# Bot do Telegram: consulta ao second brain tributário

Bot que responde, pelo Telegram, dúvidas da equipe fiscal com base nas notas deste repositório.
Roda no n8n (VPS da Hostinger), lê as notas direto do GitHub e usa a API do Claude.

## Como funciona (uma pergunta)

```
Telegram → confere o ID da pessoa → "Consultando as notas..."
  → lê os 3 INDEX.md no GitHub
  → Claude (modelo rápido) escolhe de 1 a 4 notas pelos índices   [roteador]
  → o código descarta qualquer nome que não exista nos índices
  → lê as notas escolhidas no GitHub
  → Claude (modelo mais capaz) responde só com essas notas        [prompt = regras do CLAUDE.md]
  → Telegram envia a resposta (dividida se passar de ~3.800 caracteres)
```

Formato da resposta (definido em `prompts/sistema.md`): resposta direta em 1 a 3 frases, até 4 hífens com condições
e exceções, "Atenção:" só se houver vigência/conflito/lacuna, e **"Base legal:" sempre na última linha** (norma e artigo).
Normalmente até 1.200 caracteres. Se o modelo esquecer a base legal, o código acrescenta um aviso. Nomes de nota saem
sem ".md" (o Telegram transforma "nome.md" em link para o domínio .md).

Atualizar a lei = editar as notas e dar `git push`. O bot lê sempre a versão da branch `main`.

## Arquivos

| Arquivo | Para quê |
|---|---|
| `fluxo-n8n.json` | O workflow para importar no n8n (gerado, não edite à mão) |
| `prompts/roteador.md` | Prompt do roteador (escolhe as notas) |
| `prompts/sistema.md` | Prompt da resposta (regras derivadas do `CLAUDE.md`) |
| `codigo/*.js` | Código de cada nó "Code" do n8n |
| `gerar_fluxo.py` | Junta prompts + códigos e gera o `fluxo-n8n.json` |
| `testes/testar_codigo.mjs` | Testa a lógica dos nós sem n8n e sem gastar tokens (`node testes/testar_codigo.mjs`) |

Mudou um prompt ou um código? Rode `python gerar_fluxo.py`, depois `node testes/testar_codigo.mjs` e reimporte o fluxo.
Se mudar o `CLAUDE.md` (escopo ou regras), atualize também `prompts/sistema.md` e `prompts/roteador.md`.

## Credenciais no n8n (Credentials → Create)

| Nome da credencial | Tipo | Valores |
|---|---|---|
| Telegram Bot (Consulta Fiscal) | Telegram API | Access Token do @BotFather |
| GitHub (leitura second brain) | Header Auth | Name `Authorization`, Value `Bearer <token fine-grained, só leitura, só este repositório>` |
| Anthropic API | Header Auth | Name `x-api-key`, Value `<chave da API>` |

Nunca coloque tokens no código, em prints ou em mensagens.

## Configuração (nó "Preparar")

- `USUARIOS`: os IDs do Telegram autorizados. Quem não estiver na lista recebe o próprio ID na resposta; copie para cá.
- `CFG`: dono, repositório, branch, modelos, limites de tamanho e "esforço" do modelo.
- Se a API recusar o parâmetro `effort` (erro 400), deixe `esforcoRoteador` e `esforcoResposta` como `''`.

## Travas contra consumo acidental (nó "Preparar")

Nenhuma delas chama o Claude. Ajuste em `CFG` (`maxIdadeSeg`, `minPalavras`, `minChars`, `maxPorDia`).

| Situação | O que o bot faz |
|---|---|
| Mensagem com mais de 10 min (fila acumulada com o fluxo desativado), grupo, outro bot, reenvio do mesmo `update_id`, "ok"/"obrigado" | Ignora em silêncio |
| Menos de 3 palavras ou 12 caracteres, texto começando com `@` ou `/` | Pede a pergunta completa em uma mensagem |
| Áudio, imagem ou arquivo | Pede texto |
| Mais de 60 consultas no dia pela mesma pessoa | Avisa o limite (trava aproximada) |

Cada mensagem enviada é uma consulta: oriente a equipe a escrever a pergunta inteira em **uma** mensagem.
O contador diário e a lista de reenvios ficam na memória do fluxo (`$getWorkflowStaticData`), que só persiste com o
fluxo **ativo** (não em "Execute workflow") e é aproximada quando duas consultas terminam ao mesmo tempo.
O limite firme é o de gasto do workspace no Console da Anthropic.

Vários usuários ao mesmo tempo: cada mensagem é uma execução independente do n8n e a resposta volta para o chat de
quem perguntou. Não use "Execute workflow" com o fluxo ativo: o teste troca o webhook e o bot para de responder
até reativar.

## Custo e controle

- Cada pergunta faz 2 chamadas ao Claude. O roteador recebe só os índices (~6 mil tokens) e a resposta recebe de 1 a 4 notas (limite de ~57 mil tokens no pior caso).
- Defina um limite mensal de gasto no Console da Anthropic.
- O histórico de execuções do n8n guarda pergunta, notas abertas e tokens usados (nó "Formatar resposta").

## Problemas comuns

| Sintoma | Causa provável |
|---|---|
| Bot responde "Você ainda não tem acesso" | ID não está em `USUARIOS` (use o ID mostrado na mensagem) |
| "não consegui ler os índices no GitHub (Bad credentials)" | Token do GitHub errado, expirado ou sem permissão `Contents: Read` |
| "(Not Found)" no GitHub | Dono/repositório/branch errados em `CFG`, ou token sem acesso a este repositório |
| Erro 400 da API citando `effort` ou `output_config` | Deixe os esforços vazios (`''`) em `CFG` |
| Erro 401 da API | Chave da Anthropic errada na credencial |
| Telegram não chama o fluxo | Fluxo não está ativo (chave Active), ou alguém clicou em "Execute workflow" com ele ativo: desative e ative de novo. Erro "bad webhook: An HTTPS URL must be provided": o n8n precisa estar com HTTPS e `WEBHOOK_URL` correto |
| Bot não encontra algo que existe nas notas | Veja no histórico quais notas o roteador escolheu; ajuste o índice ou o prompt do roteador |

## Limites da versão 1

- Cada pergunta é independente (sem memória de conversa): a pessoa precisa incluir o contexto na mensagem. Por isso a resposta curta não promete "detalhar": sugere o que perguntar a seguir.
- Só texto (sem áudio, imagem ou arquivo).
- Notas muito grandes são cortadas (aviso na resposta); `_mapa-regulamentos.md` tem ~122 mil caracteres.
- Não há registro por pessoa fora do histórico do n8n. Se a diretoria quiser custo por usuário, o próximo passo é gravar as consultas numa tabela.
