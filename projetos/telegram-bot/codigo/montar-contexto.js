// Nó: "Montar contexto" (Code, Run Once for All Items)
// Junta o texto das notas lidas, aplica os limites de tamanho e monta a requisição
// final (modelo mais capaz) com o prompt de sistema derivado do CLAUDE.md.
const PROMPT_SISTEMA = __PROMPT_SISTEMA__;

const p = $('Preparar').first().json;
const sel = $('Escolher notas').first().json;
const cfg = p.cfg;

// Quando não há notas escolhidas, o nó "GitHub: ler nota" não executou.
let lidas = [];
try { lidas = $('GitHub: ler nota').all(); } catch (e) { lidas = []; }

const blocos = [];
const consultadas = [];
const naoLidas = [];
const truncadas = [];
let total = 0;

sel.notas.forEach((n, i) => {
  const nome = `${n.dominio}/${n.arquivo}`;
  const it = lidas[i] && lidas[i].json;
  let t = it && typeof it.texto === 'string' ? it.texto : '';
  if (!t) { naoLidas.push(nome); return; }
  const restante = cfg.maxCharsTotal - total;
  const limite = Math.min(cfg.maxCharsNota, restante);
  if (limite <= 0) { naoLidas.push(nome); return; }
  let aviso = '';
  if (t.length > limite) {
    aviso = `\n[TRECHO FINAL OMITIDO: esta nota tem ${t.length} caracteres e foi cortada em ${limite}]`;
    truncadas.push(nome);
    t = t.slice(0, limite);
  }
  total += t.length;
  blocos.push(`<<<ARQUIVO: ${nome}>>>\n${t}${aviso}\n<<<FIM DO ARQUIVO>>>`);
  consultadas.push(nome);
});

const meta = {
  usuario: p.usuario,
  pergunta: p.pergunta,
  notasEscolhidas: sel.notas.map((n) => `${n.dominio}/${n.arquivo}`),
  descartadasPeloRoteador: sel.descartadas,
  consultadas,
  naoLidas,
  truncadas,
  caracteresEnviados: total,
  usoRoteador: sel.usoRoteador,
};

// Falha técnica: não adianta perguntar ao Claude sem a fonte.
if (sel.falha || (sel.notas.length > 0 && consultadas.length === 0)) {
  const motivo = sel.falha || 'não consegui ler as notas escolhidas no GitHub';
  return [{
    json: {
      precisaClaude: 'nao',
      mensagemDireta:
        `Não consegui consultar as notas agora: ${motivo}.\n` +
        'Tente de novo em instantes. Se o problema continuar, avise o responsável pelo second brain.',
      meta,
    },
  }];
}

const partes = [
  `Data de hoje: ${p.hoje} (use para dizer se uma regra vale hoje ou só a partir de quando).`,
  `Quem pergunta: ${p.usuario}.`,
  '',
  'PERGUNTA:',
  p.pergunta,
  '',
];
if (p.perguntaCortada) partes.push('(A pergunta foi cortada pelo limite de tamanho.)', '');
if (sel.foraEscopo) partes.push(`Nota do roteador sobre a parte fora do escopo: ${sel.foraEscopo}`);
if (sel.observacao) partes.push(`Observação do roteador: ${sel.observacao}`);
if (naoLidas.length) partes.push(`Notas escolhidas que não puderam ser lidas: ${naoLidas.join(', ')}. Avise que a resposta pode estar incompleta.`);
partes.push('');
partes.push(
  blocos.length
    ? 'NOTAS SELECIONADAS:\n\n' + blocos.join('\n\n')
    : 'NOTAS SELECIONADAS: nenhuma (o roteador não encontrou notas aplicáveis; a pergunta provavelmente está fora do escopo).'
);

const body = {
  model: cfg.modeloResposta,
  max_tokens: cfg.maxTokensResposta,
  system: PROMPT_SISTEMA,
  messages: [{ role: 'user', content: partes.join('\n') }],
};
if (cfg.esforcoResposta) body.output_config = { effort: cfg.esforcoResposta };

return [{ json: { precisaClaude: 'sim', body, meta } }];
