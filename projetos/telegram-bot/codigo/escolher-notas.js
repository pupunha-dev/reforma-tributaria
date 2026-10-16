// Nó: "Escolher notas" (Code, Run Once for All Items)
// Lê a resposta do roteador, descarta qualquer nome que não exista nos índices
// (o roteador não pode "adivinhar" arquivos) e limita a quantidade de notas.
const p = $('Preparar').first().json;
const m = $('Montar roteador').first().json;
const r = $input.first().json;

let falha = '';
let notas = [];
let foraEscopo = '';
let observacao = '';
const descartadas = [];

function textoDaResposta(resp) {
  if (!resp || !Array.isArray(resp.content)) return '';
  return resp.content.filter((b) => b.type === 'text').map((b) => b.text).join('\n').trim();
}

if (m.indicesLidos === 0) {
  falha = 'não consegui ler os índices no GitHub (' + (m.errosIndice.join('; ') || 'sem detalhe') + ')';
} else if (r.error || !Array.isArray(r.content)) {
  const e = r.error;
  falha = 'o roteador não respondeu (' + ((e && (e.message || e.description)) || JSON.stringify(r).slice(0, 200)) + ')';
} else {
  const bruto = textoDaResposta(r);
  let j = null;
  try {
    j = JSON.parse(bruto.slice(bruto.indexOf('{'), bruto.lastIndexOf('}') + 1));
  } catch (e) {
    falha = 'o roteador devolveu uma resposta ilegível';
  }
  if (j) {
    foraEscopo = String(j.fora_do_escopo || '').slice(0, 300);
    observacao = String(j.observacao || '').slice(0, 300);
    const vistos = new Set();
    for (const item of Array.isArray(j.notas) ? j.notas : []) {
      const s = String(item).trim().replace(/\\/g, '/').replace(/^notas\//, '');
      const partes = s.split('/');
      if (partes.length !== 2) { descartadas.push(s); continue; }
      const dom = partes[0];
      const arq = partes[1].replace(/\.md$/i, '');
      if (!/^[A-Za-z0-9_\-]+$/.test(arq) || !(m.validos[dom] || []).includes(arq)) {
        descartadas.push(s);
        continue;
      }
      const chave = `${dom}/${arq}`;
      if (vistos.has(chave)) continue;
      vistos.add(chave);
      notas.push({ dominio: dom, arquivo: `${arq}.md`, caminho: `notas/${dom}/${arq}.md` });
      if (notas.length >= p.cfg.maxNotas) break;
    }
  }
}

return [{
  json: {
    notas,
    falha,
    foraEscopo,
    observacao,
    descartadas,
    usoRoteador: r.usage || null,
  },
}];
