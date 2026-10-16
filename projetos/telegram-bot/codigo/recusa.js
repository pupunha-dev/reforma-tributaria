// Nó: "Mensagem sem consulta" (Code, Run Once for All Items)
// Monta a resposta para quem não tem acesso, para mensagens sem texto e para /start e /ajuda.
const p = $('Preparar').first().json;
let text;

// Mensagens a ignorar (fila velha, grupo, bot, reenvio, agradecimento): não responde nada. Sem itens, o nó seguinte não roda.
if (p.estado === 'ignorar') return [];

if (p.estado === 'sem_acesso') {
  text =
    'Você ainda não tem acesso a esta consulta.\n\n' +
    `Seu ID do Telegram é: ${p.userId}\n` +
    'Envie este número ao responsável pelo second brain para liberar o acesso.';
} else if (p.estado === 'sem_texto') {
  text = 'Envie sua dúvida em texto. Ainda não leio áudios, imagens ou arquivos.';
} else if (p.estado === 'curta') {
  text =
    'Escreva a dúvida completa em uma única mensagem, para eu consultar as notas certas.\n' +
    'Exemplo: Quando uma pessoa física vira contribuinte do IBS/CBS ao alugar imóveis?';
} else if (p.estado === 'limite_dia') {
  text =
    `Você já fez ${p.cfg.maxPorDia} consultas hoje, que é o limite diário por pessoa.\n` +
    'Volte amanhã ou fale com o responsável pelo second brain se precisar de mais.';
} else {
  text =
    `Olá, ${p.usuario}! Sou a consulta do second brain tributário do setor fiscal.\n\n` +
    'Respondo com base nas notas sobre a Reforma Tributária (LC 214/2025 e LC 227/2026), ' +
    'o Simples Nacional (LC 123/2006 e Res. CGSN 140) e os documentos fiscais eletrônicos (Notas Técnicas da NF-e).\n\n' +
    'Escreva a dúvida completa em UMA única mensagem (cada mensagem enviada gera uma consulta), por exemplo:\n' +
    '- Quando uma pessoa física vira contribuinte do IBS/CBS ao alugar imóveis?\n' +
    '- Como o crédito de IBS/CBS funciona na compra de um fornecedor do Simples?\n\n' +
    'As respostas são curtas e terminam com a base legal. Cada pergunta é independente: inclua o contexto na própria mensagem.\n' +
    'Fora do escopo: legislação estadual e municipal, IRPF e IRPJ (lucro real ou presumido).';
}

return [{ json: { chatId: p.chatId, text } }];
