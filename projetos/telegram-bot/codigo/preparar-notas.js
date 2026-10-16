// Nó: "Preparar buscas de nota" (Code, Run Once for All Items)
// Gera um item por nota escolhida, com o caminho do arquivo no repositório.
const sel = $('Escolher notas').first().json;
return sel.notas.map((n) => ({ json: n }));
