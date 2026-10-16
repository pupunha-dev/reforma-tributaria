// Nó: "Preparar buscas de índice" (Code, Run Once for All Items)
// Gera um item por domínio com o caminho do INDEX.md no repositório.
const p = $('Preparar').first().json;
return p.dominios.map((d) => ({
  json: { dominio: d, caminho: `notas/${d}/INDEX.md` },
}));
