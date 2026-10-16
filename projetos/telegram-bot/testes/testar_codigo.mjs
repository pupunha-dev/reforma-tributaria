// Testa localmente a lógica dos nós "Code" do fluxo, sem n8n e sem gastar tokens.
// Usa o código que está DENTRO do fluxo-n8n.json (o mesmo que será importado) e os índices reais do repositório.
//
//   node testes/testar_codigo.mjs
//   REPO=/caminho/do/repositorio node testes/testar_codigo.mjs   (se rodar de outro lugar)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const aqui = path.dirname(fileURLToPath(import.meta.url));
const REPO = process.env.REPO || path.resolve(aqui, '../../..');
const fluxo = JSON.parse(fs.readFileSync(path.resolve(aqui, '../fluxo-n8n.json'), 'utf8'));
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;

let ok = 0, falhas = 0;
function confere(nome, cond, detalhe = '') {
  if (cond) { ok++; console.log(`  ok   ${nome}`); }
  else { falhas++; console.log(`  FALHA ${nome} ${detalhe}`); }
}

function codigoDe(nome, trocas = []) {
  const n = fluxo.nodes.find((x) => x.name === nome);
  if (!n) throw new Error('nó não existe: ' + nome);
  let c = n.parameters.jsCode;
  for (const [de, para] of trocas) c = c.replace(de, para);
  return c;
}

// Memória simulada do n8n ($getWorkflowStaticData). null = indisponível (como em "Execute workflow" sem persistência).
let STATIC = {};
// Executa um nó Code simulando $('Nome') e $input.
async function rodar(nome, saidas, entrada, trocas = []) {
  const $ = (n) => {
    if (!(n in saidas)) throw new Error(`Node '${n}' hasn't been executed`);
    const itens = saidas[n];
    return { first: () => itens[0], all: () => itens, last: () => itens[itens.length - 1] };
  };
  const $input = { first: () => entrada[0], all: () => entrada };
  const getSD = () => { if (STATIC === null) throw new Error('static data indisponível'); return STATIC; };
  const fn = new AsyncFunction('$', '$input', '$getWorkflowStaticData', codigoDe(nome, trocas));
  const r = await fn($, $input, getSD);
  return r;
}

const ler = (rel) => {
  const f = path.join(REPO, rel);
  return fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : null;
};
let UPD = 1;
const update = (id, texto, extra = {}, msgExtra = {}) => [{ json: { update_id: extra.update_id ?? UPD++, message: { message_id: 1, from: { id, first_name: 'Teste' }, chat: { id, type: 'private' }, date: Math.floor(Date.now() / 1000), text: texto, ...msgExtra } } }];
const TROCA_ID = [["'COLE_AQUI_O_SEU_ID'", "'111'"]];

// ---------------------------------------------------------------- 1) fluxo completo
console.log('\n[1] Fluxo completo com índices reais');
{
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'Quando uma pessoa física vira contribuinte do IBS/CBS ao alugar imóveis?'), TROCA_ID);
  const p = S['Preparar'][0].json;
  confere('estado ok', p.estado === 'ok');
  confere('data de hoje no formato dd/mm/aaaa', /^\d{2}\/\d{2}\/\d{4}$/.test(p.hoje), p.hoje);

  S['Preparar buscas de índice'] = await rodar('Preparar buscas de índice', S, S['Preparar']);
  confere('3 domínios', S['Preparar buscas de índice'].length === 3);

  const indices = S['Preparar buscas de índice'].map((it) => {
    const t = ler(`notas/${it.json.dominio}/INDEX.md`);
    return { json: t ? { texto: t } : { error: { message: 'arquivo não encontrado no teste' } } };
  });
  S['GitHub: ler índice'] = indices;
  S['Montar roteador'] = await rodar('Montar roteador', S, indices);
  const mr = S['Montar roteador'][0].json;
  console.log('  validos:', Object.fromEntries(Object.entries(mr.validos).map(([k, v]) => [k, v.length])));
  confere('índices lidos = 3', mr.indicesLidos === 3, JSON.stringify(mr.errosIndice));
  confere('reforma: nota esperada existe no índice', mr.validos['reforma']?.includes('regime-especifico-bens-imoveis'));
  confere('simples-nacional (formato [[nome]]): sn-fator-r existe', mr.validos['simples-nacional']?.includes('sn-fator-r'));
  confere('documentos-fiscais (formato [[nome]]): df-danfe-reforma existe', mr.validos['documentos-fiscais']?.includes('df-danfe-reforma'));
  confere('prompt do roteador dentro do body', mr.body.system.includes('ROTEADOR'));
  confere('modelo do roteador', mr.body.model === 'claude-haiku-5-5');
  confere('effort enviado em output_config', mr.body.output_config?.effort === 'low');

  // Resposta simulada do roteador: com bloco de "thinking", nome inventado, sem extensão e tentativa de path traversal.
  const respRoteador = [{ json: {
    content: [
      { type: 'thinking', thinking: '...' },
      { type: 'text', text: 'Segue:\n{"notas": ["reforma/regime-especifico-bens-imoveis.md", "reforma/nota-inventada.md", "simples-nacional/sn-fator-r", "../../etc/passwd", "reforma/regime-especifico-bens-imoveis.md"], "fora_do_escopo": "IR do aluguel", "observacao": ""}' },
    ],
    usage: { input_tokens: 5000, output_tokens: 120 },
  } }];
  S['Claude: roteador'] = respRoteador;
  S['Escolher notas'] = await rodar('Escolher notas', S, respRoteador);
  const es = S['Escolher notas'][0].json;
  confere('2 notas válidas (duplicada e inventadas descartadas)', es.notas.length === 2, JSON.stringify(es.notas));
  confere('inventadas ficaram em descartadas', es.descartadas.length === 2, JSON.stringify(es.descartadas));
  confere('aceita nome sem .md', es.notas.some((n) => n.caminho === 'notas/simples-nacional/sn-fator-r.md'));
  confere('sem falha', es.falha === '');

  S['Preparar buscas de nota'] = await rodar('Preparar buscas de nota', S, S['Escolher notas']);
  confere('2 itens para buscar', S['Preparar buscas de nota'].length === 2);

  // GitHub devolve a nota que existe localmente; sn-fator-r simula 404 (mesmo que exista no disco).
  const notas = S['Preparar buscas de nota'].map((it) => {
    const t = it.json.caminho.includes('sn-fator-r') ? null : ler(it.json.caminho);
    return { json: t ? { texto: t } : { error: { message: '404 Not Found' } } };
  });
  S['GitHub: ler nota'] = notas;
  S['Montar contexto'] = await rodar('Montar contexto', S, notas);
  const mc = S['Montar contexto'][0].json;
  confere('precisaClaude = sim', mc.precisaClaude === 'sim');
  const conteudo = mc.body.messages[0].content;
  confere('nota lida entrou no contexto', conteudo.includes('<<<ARQUIVO: reforma/regime-especifico-bens-imoveis.md>>>') && conteudo.includes('R$ 240 mil'));
  confere('nota não lida foi sinalizada', mc.meta.naoLidas.includes('simples-nacional/sn-fator-r.md') && conteudo.includes('não puderam ser lidas'));
  confere('nota do roteador sobre fora do escopo repassada', conteudo.includes('IR do aluguel'));
  confere('prompt de sistema com regras do CLAUDE.md', mc.body.system.includes('SOMENTE') && mc.body.system.includes('Hierarquia'));
  confere('modelo da resposta', mc.body.model === 'claude-sonnet-5-5');

  const respClaude = [{ json: {
    content: [{ type: 'thinking', thinking: '...' }, { type: 'text', text: '**Resposta**\n\n# Título\n- A pessoa física vira contribuinte se...\n\nVeja regime-especifico-bens-imoveis.md.\n\nBase legal: LC 214/2025, art. 251, §§ 1º e 2º' }],
    usage: { input_tokens: 9000, output_tokens: 400 }, stop_reason: 'end_turn',
  } }];
  S['Claude: resposta'] = respClaude;
  const fm = await rodar('Formatar resposta', S, respClaude);
  confere('1 mensagem', fm.length === 1);
  const t = fm[0].json.text;
  confere('markdown removido', !t.includes('**') && !/^#/m.test(t));
  confere('rodapé com notas abertas (sem .md)', t.includes('Notas abertas: regime-especifico-bens-imoveis') && !t.includes('.md'));
  confere('nome de nota no texto sem .md (evita link do Telegram)', t.includes('Veja regime-especifico-bens-imoveis.') && !/\.md\b/.test(t));
  confere('base legal mantida', t.includes('Base legal: LC 214/2025, art. 251'));
  confere('não duplica base legal quando o modelo já escreveu', (t.match(/Base legal/gi) || []).length === 1);
  confere('rodapé de aviso', t.includes('não substitui a análise do caso concreto'));
  confere('chatId preservado', fm[0].json.chatId === 111);
  confere('uso de tokens registrado', fm[0].json.meta?.usoResposta?.output_tokens === 400 && fm[0].json.meta?.usoRoteador?.input_tokens === 5000);
}

// ---------------------------------------------------------------- 2) acesso
console.log('\n[2] Acesso e comandos');
{
  let S = {};
  S['Preparar'] = await rodar('Preparar', S, update(999, 'oi'), TROCA_ID);
  confere('ID fora da lista = sem_acesso', S['Preparar'][0].json.estado === 'sem_acesso');
  let r = await rodar('Mensagem sem consulta', S, S['Preparar']);
  confere('resposta mostra o ID da pessoa', r[0].json.text.includes('999'));

  S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, '/start'), TROCA_ID);
  confere('/start = ajuda', S['Preparar'][0].json.estado === 'ajuda');
  r = await rodar('Mensagem sem consulta', S, S['Preparar']);
  confere('texto de ajuda', r[0].json.text.includes('Olá, Daniel'));

  S = {};
  const semTexto = update(111, '');
  delete semTexto[0].json.message.text;
  S['Preparar'] = await rodar('Preparar', S, semTexto, TROCA_ID);
  confere('mensagem sem texto', S['Preparar'][0].json.estado === 'sem_texto');

  S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'palavra '.repeat(1000)), TROCA_ID);
  confere('pergunta longa é cortada', S['Preparar'][0].json.pergunta.length === 1500 && S['Preparar'][0].json.perguntaCortada);
}

// ---------------------------------------------------------------- 3) falhas
console.log('\n[3] Falhas técnicas');
{
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'pergunta de teste sobre imóveis'), TROCA_ID);
  S['Preparar buscas de índice'] = await rodar('Preparar buscas de índice', S, S['Preparar']);
  // GitHub fora do ar / token inválido
  const ruins = S['Preparar buscas de índice'].map(() => ({ json: { error: { message: 'Bad credentials' } } }));
  S['GitHub: ler índice'] = ruins;
  S['Montar roteador'] = await rodar('Montar roteador', S, ruins);
  confere('sem índices: indicesLidos = 0', S['Montar roteador'][0].json.indicesLidos === 0);
  S['Escolher notas'] = await rodar('Escolher notas', S, [{ json: { content: [{ type: 'text', text: '{}' }] } }]);
  confere('falha de GitHub reportada', S['Escolher notas'][0].json.falha.includes('Bad credentials'));
  S['Montar contexto'] = await rodar('Montar contexto', S, S['Escolher notas']);
  confere('não chama o Claude', S['Montar contexto'][0].json.precisaClaude === 'nao');
  const fm = await rodar('Formatar resposta', S, S['Montar contexto']);
  confere('usuário recebe aviso claro', fm[0].json.text.includes('Não consegui consultar as notas agora'));
  confere('sem rodapé de "notas abertas" em falha', !fm[0].json.text.includes('Notas abertas'));
}
{
  // Roteador devolve lixo e depois erro da API
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'pergunta de teste sobre imóveis'), TROCA_ID);
  S['Montar roteador'] = [{ json: { indicesLidos: 3, validos: { reforma: ['a'] }, errosIndice: [] } }];
  let e = await rodar('Escolher notas', S, [{ json: { content: [{ type: 'text', text: 'não sei' }] } }]);
  confere('roteador ilegível = falha', e[0].json.falha.includes('ilegível'));
  e = await rodar('Escolher notas', S, [{ json: { error: { message: '529 overloaded' } } }]);
  confere('erro de API do roteador = falha', e[0].json.falha.includes('529'));
  // Erro da API na resposta final
  S['Escolher notas'] = [{ json: { notas: [], falha: '', foraEscopo: '', observacao: '', descartadas: [] } }];
  S['Montar contexto'] = await rodar('Montar contexto', S, S['Escolher notas']);
  confere('sem notas e sem falha: ainda chama o Claude (pergunta fora do escopo)', S['Montar contexto'][0].json.precisaClaude === 'sim');
  confere('mensagem avisa que não há notas aplicáveis', S['Montar contexto'][0].json.body.messages[0].content.includes('nenhuma'));
  const fm = await rodar('Formatar resposta', S, [{ json: { error: { message: '401 invalid x-api-key' } } }]);
  confere('erro da API final vira mensagem amigável com detalhe', fm[0].json.text.includes('problema técnico') && fm[0].json.text.includes('401'));
}

// ---------------------------------------------------------------- 4) limites
console.log('\n[4] Limites de tamanho');
{
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'pergunta de teste sobre imóveis'), TROCA_ID);
  S['Escolher notas'] = [{ json: { notas: [
    { dominio: 'reforma', arquivo: 'grande.md' }, { dominio: 'reforma', arquivo: 'outra.md' }, { dominio: 'reforma', arquivo: 'terceira.md' },
  ], falha: '', foraEscopo: '', observacao: '', descartadas: [], usoRoteador: null } }];
  const lidas = [{ json: { texto: 'a'.repeat(120000) } }, { json: { texto: 'b'.repeat(80000) } }, { json: { texto: 'c'.repeat(80000) } }];
  S['GitHub: ler nota'] = lidas;
  const mc = (await rodar('Montar contexto', S, lidas))[0].json;
  confere('nota grande cortada em 80.000 e marcada', mc.meta.truncadas.includes('reforma/grande.md') && mc.body.messages[0].content.includes('TRECHO FINAL OMITIDO'));
  confere('total respeita 200.000', mc.meta.caracteresEnviados <= 200000, String(mc.meta.caracteresEnviados));
  confere('3ª nota ficou truncada pelo total (40.000)', mc.meta.truncadas.includes('reforma/terceira.md'));
}
{
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'pergunta de teste sobre imóveis'), TROCA_ID);
  S['Montar contexto'] = [{ json: { precisaClaude: 'sim', meta: { consultadas: ['reforma/a.md'], truncadas: [] } } }];
  const longo = ('Parágrafo de teste com algum texto.\n\n').repeat(300); // ~10.800 caracteres
  const fm = await rodar('Formatar resposta', S, [{ json: { content: [{ type: 'text', text: longo }], stop_reason: 'end_turn', usage: {} } }]);
  confere('resposta longa dividida em várias mensagens', fm.length >= 3, String(fm.length));
  confere('nenhuma mensagem passa de 4.096', fm.every((x) => x.json.text.length <= 4096), fm.map((x) => x.json.text.length).join(','));
}

// ---------------------------------------------------------------- 5) base legal sempre
console.log('\n[5] Base legal e prompt curto');
{
  const S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'pergunta de teste sobre imóveis'), TROCA_ID);
  S['Montar contexto'] = [{ json: { precisaClaude: 'sim', meta: { consultadas: ['reforma/a.md'], truncadas: [] } } }];
  const fm = await rodar('Formatar resposta', S, [{ json: { content: [{ type: 'text', text: 'Resposta curta sem base legal.' }], stop_reason: 'end_turn', usage: {} } }]);
  confere('modelo esqueceu a base legal: o código acrescenta', /Base legal:/.test(fm[0].json.text));
  const fm2 = await rodar('Formatar resposta', S, [{ json: { error: { message: '500' } } }]);
  confere('mensagem de erro técnico não ganha base legal', !/Base legal:/.test(fm2[0].json.text));
  const mc = codigoDe('Montar contexto');
  confere('prompt de sistema exige base legal e formato curto', mc.includes('BASE LEGAL') && mc.includes('Base legal:') && mc.includes('1.200'));
}

// ---------------------------------------------------------------- 6) travas contra disparo acidental
console.log('\n[6] Travas anti-disparo');
{
  const est = async (entrada, sd = {}) => { STATIC = sd; const S = {}; S['Preparar'] = await rodar('Preparar', S, entrada, TROCA_ID); return [S['Preparar'][0].json.estado, S]; };
  const agora = Math.floor(Date.now() / 1000);

  confere('pergunta normal = ok', (await est(update(111, 'Qual o limite do Simples Nacional em 2027?')))[0] === 'ok');
  confere('mensagem com 11 min = ignorar', (await est(update(111, 'Qual o limite do Simples Nacional em 2027?', {}, { date: agora - 660 })))[0] === 'ignorar');
  confere('mensagem velha de quem não tem acesso também é ignorada (sem flood)', (await est(update(999, 'oi tudo bem com você', {}, { date: agora - 3600 })))[0] === 'ignorar');
  confere('grupo = ignorar', (await est(update(111, 'Qual o limite do Simples Nacional em 2027?', {}, { chat: { id: -5, type: 'supergroup' } })))[0] === 'ignorar');
  confere('bot = ignorar', (await est(update(111, 'Qual o limite do Simples Nacional em 2027?', {}, { from: { id: 111, is_bot: true } })))[0] === 'ignorar');
  confere('agradecimento = ignorar', (await est(update(111, 'Obrigado!')))[0] === 'ignorar');
  confere('"IBS" = curta (sem Claude)', (await est(update(111, 'IBS')))[0] === 'curta');
  confere('"fator r" = curta', (await est(update(111, 'fator r')))[0] === 'curta');
  confere('"@userinfobot" = curta', (await est(update(111, '@userinfobot')))[0] === 'curta');
  confere('"/userinfobot" = curta', (await est(update(111, '/userinfobot')))[0] === 'curta');
  confere('3 palavras já passam', (await est(update(111, 'alíquota do IBS')))[0] === 'ok');
  confere('/start continua = ajuda', (await est(update(111, '/start')))[0] === 'ajuda');

  // reenvio do mesmo update_id
  STATIC = {};
  const igual = update(111, 'Qual o limite do Simples Nacional em 2027?', { update_id: 777 });
  let S1 = {}; S1['Preparar'] = await rodar('Preparar', S1, igual, TROCA_ID);
  let S2 = {}; S2['Preparar'] = await rodar('Preparar', S2, igual, TROCA_ID);
  confere('1ª vez ok, reenvio do Telegram = ignorar', S1['Preparar'][0].json.estado === 'ok' && S2['Preparar'][0].json.estado === 'ignorar');

  // teto diário por pessoa
  const hojeBR = new Date(Date.now() - 3 * 3600 * 1000).toISOString().slice(0, 10).split('-').reverse().join('/');
  const [e60] = await est(update(111, 'Qual o limite do Simples Nacional em 2027?'), { uso: { dia: hojeBR, por: { '111': 60 } } });
  confere('61ª consulta do dia = limite_dia', e60 === 'limite_dia');
  const [eOutro] = await est(update(111, 'Qual o limite do Simples Nacional em 2027?'), { uso: { dia: '01/01/2020', por: { '111': 60 } } });
  confere('contagem zera no dia seguinte', eOutro === 'ok');
  const [eSem] = await (async () => { STATIC = null; const S = {}; S['Preparar'] = await rodar('Preparar', S, update(111, 'Qual o limite do Simples Nacional em 2027?'), TROCA_ID); return [S['Preparar'][0].json.estado]; })();
  confere('sem memória disponível o bot continua funcionando', eSem === 'ok');
  STATIC = {};

  // respostas dos novos estados
  let S = {};
  S['Preparar'] = await rodar('Preparar', S, update(111, 'x', {}, {}), TROCA_ID);
  S['Preparar'][0].json.estado = 'ignorar';
  confere('ignorar não gera mensagem', (await rodar('Mensagem sem consulta', S, S['Preparar'])).length === 0);
  S['Preparar'][0].json.estado = 'curta';
  confere('curta pede a pergunta completa', (await rodar('Mensagem sem consulta', S, S['Preparar']))[0].json.text.includes('única mensagem'));
  S['Preparar'][0].json.estado = 'limite_dia';
  confere('limite_dia informa o teto', (await rodar('Mensagem sem consulta', S, S['Preparar']))[0].json.text.includes('60 consultas'));
}

console.log(`\nResultado: ${ok} ok, ${falhas} falha(s)`);
process.exit(falhas ? 1 : 0);
