// Nó: "Formatar resposta" (Code, Run Once for All Items)
// Extrai o texto da resposta do Claude, limpa marcações de markdown, acrescenta o rodapé
// e divide em mensagens de até ~3.800 caracteres (o limite do Telegram é 4.096).
const p = $('Preparar').first().json;
const ctx = $('Montar contexto').first().json;
const inp = $input.first().json;

let corpo = '';
let usoResposta = null;
let stop = '';
let doModelo = false;

if (ctx.mensagemDireta) {
  corpo = ctx.mensagemDireta;
} else if (inp.error || !Array.isArray(inp.content)) {
  const e = inp.error;
  const detalhe = (e && (e.message || e.description)) || '';
  corpo =
    'Tive um problema técnico ao gerar a resposta. Tente de novo em instantes. ' +
    'Se continuar, avise o responsável pelo second brain.' +
    (detalhe ? `\n(Detalhe técnico: ${String(detalhe).slice(0, 200)})` : '');
} else {
  corpo = inp.content.filter((b) => b.type === 'text').map((b) => b.text).join('\n').trim();
  doModelo = !!corpo;
  usoResposta = inp.usage || null;
  stop = inp.stop_reason || '';
  if (!corpo) corpo = 'O modelo não devolveu texto. Reformule a pergunta e tente de novo.';
  if (stop === 'max_tokens') corpo += '\n\n(Resposta cortada pelo limite de tamanho. Peça um ponto específico para detalhar.)';
  if (stop === 'refusal') corpo = 'Não consegui responder a esta pergunta.';
}

// Telegram em texto simples: remove marcações de markdown que o modelo eventualmente use.
corpo = corpo.replace(/\*\*/g, '').replace(/^#{1,6}\s+/gm, '').replace(/^\s*```.*$/gm, '').trim();
// ".md" é um domínio de internet: o Telegram transformaria "nome.md" em link clicável. Tira a extensão.
const semMd = (s) => s.replace(/([A-Za-z0-9_\-]+)\.md\b/gi, '$1');
corpo = semMd(corpo);
// Toda resposta do modelo precisa terminar com a base legal (o prompt exige; aqui é a garantia).
if (doModelo && stop !== 'refusal' && !/base legal\s*:/i.test(corpo)) {
  corpo += '\n\nBase legal: não indicada na resposta; confira nas notas abertas abaixo.';
}

let rodape = '';
if (!ctx.mensagemDireta && ctx.meta && ctx.meta.consultadas && ctx.meta.consultadas.length) {
  const nomes = ctx.meta.consultadas.map((n) => semMd(n.split('/').pop()));
  rodape += `\n\nNotas abertas: ${nomes.join(', ')}`;
  if (ctx.meta.truncadas && ctx.meta.truncadas.length) rodape += ' (algumas foram cortadas pelo limite de tamanho)';
}
if (!ctx.mensagemDireta) rodape += '\nConsulta de apoio; não substitui a análise do caso concreto.';

const texto = corpo + rodape;

function dividir(t, max) {
  const out = [];
  let resto = t;
  while (resto.length > max) {
    let corte = resto.lastIndexOf('\n\n', max);
    if (corte < max * 0.5) corte = resto.lastIndexOf('\n', max);
    if (corte < max * 0.5) corte = resto.lastIndexOf(' ', max);
    if (corte <= 0) corte = max;
    out.push(resto.slice(0, corte).trim());
    resto = resto.slice(corte).trim();
  }
  if (resto) out.push(resto);
  return out;
}

const meta = {
  ...(ctx.meta || {}),
  usoResposta,
  stopReason: stop,
};

// O nó do Telegram envia com parse_mode Markdown (padrão do n8n). Um "_", "*", "`" ou "[" solto no texto
// (ex.: "IndOp_IBSCBS") faz o Telegram recusar a mensagem inteira ("can't parse entities").
// A barra invertida antes do caractere o mantém como texto comum. Escapa depois de dividir (cada parte
// continua abaixo de 4.096 caracteres: o corte é em 3.800).
const escapar = (s) => s.replace(/([_*`\[])/g, '\\$1');

return dividir(texto, 3800).map((t, i, arr) => ({
  json: { chatId: p.chatId, text: escapar(t), parte: i + 1, partes: arr.length, meta: i === 0 ? meta : undefined },
}));
