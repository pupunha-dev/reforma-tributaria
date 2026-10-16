#!/usr/bin/env python3
"""Gera o arquivo fluxo-n8n.json (workflow do n8n) a partir de:

  prompts/roteador.md   prompt do roteador (modelo rápido que escolhe as notas)
  prompts/sistema.md    prompt de sistema da resposta (regras derivadas do CLAUDE.md)
  codigo/*.js           código de cada nó "Code" do n8n

Quando você alterar um prompt ou um código, rode de novo:

    python gerar_fluxo.py

e reimporte o fluxo no n8n (ou copie o trecho alterado para o nó correspondente).
"""
import json
import uuid
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
NS = uuid.UUID("5f0c1a52-9d1e-4c7b-8a53-0b9e2f1c7d11")  # ids estáveis entre execuções


def uid(nome: str) -> str:
    return str(uuid.uuid5(NS, nome))


def ler(caminho: str) -> str:
    return (RAIZ / caminho).read_text(encoding="utf-8")


def js(caminho: str) -> str:
    codigo = ler(caminho)
    if "__PROMPT_ROTEADOR__" in codigo:
        codigo = codigo.replace("__PROMPT_ROTEADOR__", json.dumps(ler("prompts/roteador.md").strip(), ensure_ascii=False))
    if "__PROMPT_SISTEMA__" in codigo:
        codigo = codigo.replace("__PROMPT_SISTEMA__", json.dumps(ler("prompts/sistema.md").strip(), ensure_ascii=False))
    return codigo


CRED_TELEGRAM = {"telegramApi": {"name": "Telegram Bot (Consulta Fiscal)"}}
CRED_GITHUB = {"httpHeaderAuth": {"name": "GitHub (leitura second brain)"}}
CRED_ANTHROPIC = {"httpHeaderAuth": {"name": "Anthropic API"}}

nodes = []
posicao = {"x": 0, "y": 0}


def add(node, x, y):
    node["id"] = uid(node["name"])
    node["position"] = [x, y]
    nodes.append(node)


def code_node(nome, arquivo):
    return {
        "name": nome,
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "parameters": {"mode": "runOnceForAllItems", "language": "javaScript", "jsCode": js(arquivo)},
    }


def if_node(nome, esquerda, operador, direita):
    return {
        "name": nome,
        "type": "n8n-nodes-base.if",
        "typeVersion": 2.2,
        "parameters": {
            "conditions": {
                "options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                "conditions": [
                    {
                        "id": uid(nome + "/cond"),
                        "leftValue": esquerda,
                        "rightValue": direita,
                        "operator": operador,
                    }
                ],
                "combinator": "and",
            },
            "options": {},
        },
    }


def telegram_send(nome, chat_id_expr, texto_expr):
    return {
        "name": nome,
        "type": "n8n-nodes-base.telegram",
        "typeVersion": 1.2,
        "parameters": {
            "resource": "message",
            "operation": "sendMessage",
            "chatId": chat_id_expr,
            "text": texto_expr,
            "additionalFields": {"appendAttribution": False},
        },
        "credentials": CRED_TELEGRAM,
        "webhookId": uid(nome + "/webhook"),
    }


URL_GITHUB = (
    "=https://api.github.com/repos/{{ $('Preparar').first().json.cfg.owner }}"
    "/{{ $('Preparar').first().json.cfg.repo }}/contents/{{ $json.caminho }}"
    "?ref={{ $('Preparar').first().json.cfg.branch }}"
)


def github_get(nome):
    return {
        "name": nome,
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "parameters": {
            "method": "GET",
            "url": URL_GITHUB,
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": True,
            "headerParameters": {
                "parameters": [
                    {"name": "Accept", "value": "application/vnd.github.raw+json"},
                    {"name": "X-GitHub-Api-Version", "value": "2022-11-28"},
                ]
            },
            "options": {
                "response": {"response": {"responseFormat": "text", "outputPropertyName": "texto"}},
                "timeout": 60000,
            },
        },
        "credentials": CRED_GITHUB,
        "retryOnFail": True,
        "maxTries": 2,
        "waitBetweenTries": 2000,
        "onError": "continueRegularOutput",
    }


def claude_post(nome):
    return {
        "name": nome,
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "parameters": {
            "method": "POST",
            "url": "https://api.anthropic.com/v1/messages",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": True,
            "headerParameters": {"parameters": [{"name": "anthropic-version", "value": "2023-06-01"}]},
            "sendBody": True,
            "specifyBody": "json",
            "jsonBody": "={{ JSON.stringify($json.body) }}",
            "options": {"timeout": 180000},
        },
        "credentials": CRED_ANTHROPIC,
        "retryOnFail": True,
        "maxTries": 2,
        "waitBetweenTries": 3000,
        "onError": "continueRegularOutput",
    }


# ---------------------------------------------------------------- nós
LEIA_ME = (
    "## Second brain tributário no Telegram\n\n"
    "**Antes de ativar:**\n"
    "1. Credencial **Telegram Bot (Consulta Fiscal)**: token do @BotFather.\n"
    "2. Credencial **GitHub (leitura second brain)**: tipo Header Auth, nome `Authorization`, "
    "valor `Bearer SEU_TOKEN` (token fine-grained, só leitura, só este repositório).\n"
    "3. Credencial **Anthropic API**: tipo Header Auth, nome `x-api-key`, valor = sua chave.\n"
    "4. No nó **Preparar**, troque `COLE_AQUI_O_SEU_ID` pelo seu ID do Telegram e confira dono/repositório/branch.\n"
    "5. Teste com **Execute workflow** e mande uma mensagem ao bot; depois ative o fluxo (chave Active).\n\n"
    "Os prompts estão dentro dos nós **Montar roteador** e **Montar contexto** "
    "(gerados a partir de prompts/*.md pelo gerar_fluxo.py)."
)
add(
    {
        "name": "Leia-me",
        "type": "n8n-nodes-base.stickyNote",
        "typeVersion": 1,
        "parameters": {"content": LEIA_ME, "height": 380, "width": 520, "color": 5},
    },
    -300, -520,
)

add(
    {
        "name": "Telegram Trigger",
        "type": "n8n-nodes-base.telegramTrigger",
        "typeVersion": 1.2,
        "parameters": {"updates": ["message"], "additionalFields": {}},
        "credentials": CRED_TELEGRAM,
        "webhookId": uid("Telegram Trigger/webhook"),
    },
    0, 0,
)
add(code_node("Preparar", "codigo/preparar.js"), 240, 0)
add(if_node("Autorizado?", "={{ $json.estado }}", {"type": "string", "operation": "equals"}, "ok"), 480, 0)

add(code_node("Mensagem sem consulta", "codigo/recusa.js"), 740, 220)
add(
    telegram_send("Telegram: enviar aviso", "={{ $json.chatId }}", "={{ $json.text }}"),
    980, 220,
)

add(
    telegram_send(
        "Telegram: consultando",
        "={{ $('Preparar').first().json.chatId }}",
        "Consultando as notas, um instante...",
    ),
    740, -120,
)
add(code_node("Preparar buscas de índice", "codigo/indices-buscas.js"), 980, -120)
add(github_get("GitHub: ler índice"), 1220, -120)
add(code_node("Montar roteador", "codigo/montar-roteador.js"), 1460, -120)
add(claude_post("Claude: roteador"), 1700, -120)
add(code_node("Escolher notas", "codigo/escolher-notas.js"), 1940, -120)
add(
    if_node("Há notas?", "={{ $json.notas.length }}", {"type": "number", "operation": "gt"}, 0),
    2180, -120,
)
add(code_node("Preparar buscas de nota", "codigo/preparar-notas.js"), 2420, -240)
add(github_get("GitHub: ler nota"), 2660, -240)
add(code_node("Montar contexto", "codigo/montar-contexto.js"), 2900, -120)
add(
    if_node("Chamar Claude?", "={{ $json.precisaClaude }}", {"type": "string", "operation": "equals"}, "sim"),
    3140, -120,
)
add(claude_post("Claude: resposta"), 3380, -240)
add(code_node("Formatar resposta", "codigo/formatar-resposta.js"), 3620, -120)
add(
    telegram_send("Telegram: enviar resposta", "={{ $json.chatId }}", "={{ $json.text }}"),
    3860, -120,
)

# ---------------------------------------------------------------- conexões
def lig(origem, *saidas):
    """saidas: lista de listas de destinos, uma lista por saída do nó."""
    return {
        origem: {
            "main": [[{"node": d, "type": "main", "index": 0} for d in destinos] for destinos in saidas]
        }
    }


conexoes = {}
for c in (
    lig("Telegram Trigger", ["Preparar"]),
    lig("Preparar", ["Autorizado?"]),
    lig("Autorizado?", ["Telegram: consultando"], ["Mensagem sem consulta"]),
    lig("Mensagem sem consulta", ["Telegram: enviar aviso"]),
    lig("Telegram: consultando", ["Preparar buscas de índice"]),
    lig("Preparar buscas de índice", ["GitHub: ler índice"]),
    lig("GitHub: ler índice", ["Montar roteador"]),
    lig("Montar roteador", ["Claude: roteador"]),
    lig("Claude: roteador", ["Escolher notas"]),
    lig("Escolher notas", ["Há notas?"]),
    lig("Há notas?", ["Preparar buscas de nota"], ["Montar contexto"]),
    lig("Preparar buscas de nota", ["GitHub: ler nota"]),
    lig("GitHub: ler nota", ["Montar contexto"]),
    lig("Montar contexto", ["Chamar Claude?"]),
    lig("Chamar Claude?", ["Claude: resposta"], ["Formatar resposta"]),
    lig("Claude: resposta", ["Formatar resposta"]),
    lig("Formatar resposta", ["Telegram: enviar resposta"]),
):
    conexoes.update(c)

workflow = {
    "name": "Second Brain Tributário - Telegram",
    "nodes": nodes,
    "connections": conexoes,
    "pinData": {},
    "settings": {"executionOrder": "v1"},
    "active": False,
}

saida = RAIZ / "fluxo-n8n.json"
saida.write_text(json.dumps(workflow, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"OK: {saida.name} com {len(nodes)} nós")
