// Nó: "Montar roteador" (Code, Run Once for All Items)
// Junta os índices lidos do GitHub, descobre quais notas existem em cada domínio
// e monta a requisição do roteador (modelo rápido) para a API do Claude.
const PROMPT_ROTEADOR = __PROMPT_ROTEADOR__;

const p = $('Preparar').first().json;
const cfg = p.cfg;
const buscas = $('Preparar buscas de índice').all();
const itens = $input.all();

let indicesTexto = '';
const validos = {};
const erros = [];

itens.forEach((it, i) => {
  const dom = buscas[i].json.dominio;
  const texto = typeof it.json.texto === 'string' ? it.json.texto : '';
  if (!texto) {
    const e = it.json.error;
    erros.push(`${dom}: ${(e && (e.message || e.description)) || e || 'sem conteúdo'}`);
    return;
  }
  indicesTexto += `\n=== DOMÍNIO: ${dom} (arquivos em notas/${dom}/) ===\n${texto}\n`;
  const nomes = new Set();
  // Formato da reforma: [nome.md](nome.md)
  for (const m of texto.matchAll(/\]\(([A-Za-z0-9_\-]+)\.md\)/g)) nomes.add(m[1]);
  // Formato do simples-nacional e documentos-fiscais: [[nome]]
  for (const m of texto.matchAll(/\[\[([A-Za-z0-9_\-]+)\]\]/g)) nomes.add(m[1]);
  validos[dom] = [...nomes];
});

const usuarioTexto = `PERGUNTA:\n${p.pergunta}\n\nÍNDICES DAS NOTAS:\n${indicesTexto}`;
const body = {
  model: cfg.modeloRoteador,
  max_tokens: cfg.maxTokensRoteador,
  system: PROMPT_ROTEADOR,
  messages: [{ role: 'user', content: usuarioTexto }],
};
if (cfg.esforcoRoteador) body.output_config = { effort: cfg.esforcoRoteador };

return [{
  json: {
    body,
    validos,
    indicesLidos: Object.keys(validos).length,
    errosIndice: erros,
  },
}];
