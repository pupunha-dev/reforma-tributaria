// Nó: "Preparar" (Code, Run Once for All Items)
// Lê a mensagem do Telegram, confere se a pessoa está autorizada e reúne a configuração do fluxo.

// ===================== CONFIGURAÇÃO (edite aqui) =====================
// Usuários autorizados: 'ID numérico do Telegram': 'Nome'.
// Quem não estiver aqui recebe o próprio ID na resposta, para você copiar para cá.
const USUARIOS = {
  'COLE_AQUI_O_SEU_ID': 'Daniel',
  // '123456789': 'Fulana',
};

const CFG = {
  owner: 'pupunha-dev',            // dono do repositório no GitHub
  repo: 'reforma-tributaria',      // nome do repositório
  branch: 'main',                  // branch lida pelo bot
  modeloRoteador: 'claude-haiku-5-5',
  modeloResposta: 'claude-sonnet-5-5',
  esforcoRoteador: 'low',          // 'low' | 'medium' | 'high'; deixe '' para não enviar o parâmetro
  esforcoResposta: 'medium',       // idem
  maxTokensRoteador: 2000,         // inclui o "raciocínio" do modelo, por isso é folgado
  maxTokensResposta: 8000,
  maxNotas: 6,                     // notas abertas por pergunta (o corte por tamanho total abaixo continua valendo)
  maxCharsNota: 80000,             // corte por nota (~23 mil tokens)
  maxCharsTotal: 200000,           // corte do total de notas (~57 mil tokens)
  maxCharsPergunta: 1500,
  // Travas contra consumo acidental de tokens (nada disso chama o Claude):
  maxIdadeSeg: 600,                // ignora em silêncio mensagens com mais de 10 min (fila acumulada com o bot parado)
  minPalavras: 3,                  // abaixo disso (ou de minChars) o bot só pede a pergunta completa
  minChars: 12,
  maxPorDia: 60,                   // consultas por pessoa por dia (0 = sem limite). Trava aproximada; o limite firme é o de gasto no Console da Anthropic
};
const DOMINIOS = ['reforma', 'simples-nacional', 'documentos-fiscais'];
// =====================================================================

const upd = $input.first().json;
const msg = upd.message || upd.edited_message || {};
const de = msg.from || {};
const id = String(de.id ?? '');
const chatId = msg.chat?.id ?? de.id;
const texto = (msg.text || '').trim();
const nomeTelegram = [de.first_name, de.last_name].filter(Boolean).join(' ');

// Estatísticas de apoio (só leitura da mensagem).
const palavras = texto.split(/\s+/).filter(Boolean).length;
const idadeSeg = msg.date ? Math.floor(Date.now() / 1000 - msg.date) : 0; // sem data (testes): trata como recente
const agradecimento = /^(ok|certo|beleza|blz|show|perfeito|entendi|valeu|obrigad[oa]|muito obrigad[oa]|gratid[aã]o|👍|🙏)[\s!.,]*$/i;

// Memória curta entre execuções (só funciona com o fluxo ativo; em "Execute workflow" não persiste).
let sd = null;
try { sd = $getWorkflowStaticData('global'); } catch (e) { sd = null; }

// "ignorar" = não responde nada e não gasta nada. A ordem importa.
let estado = 'ok';
if (msg.chat && msg.chat.type && msg.chat.type !== 'private') estado = 'ignorar';      // grupos/canais
else if (de.is_bot) estado = 'ignorar';
else if (idadeSeg > CFG.maxIdadeSeg) estado = 'ignorar';                               // fila velha
else if (sd && upd.update_id !== undefined && (sd.vistos || []).includes(upd.update_id)) estado = 'ignorar'; // reenvio do Telegram
else if (!id || !Object.prototype.hasOwnProperty.call(USUARIOS, id)) estado = 'sem_acesso';
else if (!texto) estado = 'sem_texto';
else if (/^\/(start|ajuda|help)(@\w+)?\s*$/i.test(texto)) estado = 'ajuda';
else if (agradecimento.test(texto)) estado = 'ignorar';
else if (texto.startsWith('/') || texto.startsWith('@') || palavras < CFG.minPalavras || texto.length < CFG.minChars) estado = 'curta';

// Registro de update_id (anti-duplicidade) e contagem diária por pessoa.
const brData = new Date(Date.now() - 3 * 3600 * 1000).toISOString().slice(0, 10).split('-');
const hoje = `${brData[2]}/${brData[1]}/${brData[0]}`;
let usoHoje = 0;
if (sd) {
  try {
    if (upd.update_id !== undefined) sd.vistos = [...(sd.vistos || []), upd.update_id].slice(-100);
    if (!sd.uso || sd.uso.dia !== hoje) sd.uso = { dia: hoje, por: {} };
    if (estado === 'ok') {
      usoHoje = (sd.uso.por[id] || 0) + 1;
      if (CFG.maxPorDia > 0 && usoHoje > CFG.maxPorDia) estado = 'limite_dia';
      else sd.uso.por[id] = usoHoje;
    }
  } catch (e) { /* sem memória: segue sem as travas de contagem */ }
}

return [{
  json: {
    estado,
    chatId,
    userId: id,
    usuario: USUARIOS[id] || nomeTelegram || 'colega',
    nomeTelegram,
    pergunta: texto.slice(0, CFG.maxCharsPergunta),
    perguntaCortada: texto.length > CFG.maxCharsPergunta,
    hoje,
    usoHoje,
    cfg: CFG,
    dominios: DOMINIOS,
  },
}];
