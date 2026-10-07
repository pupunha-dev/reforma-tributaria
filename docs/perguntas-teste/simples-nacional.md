# Perguntas-teste — domínio simples-nacional

Rodar depois de qualquer mudança nas notas `sn-*`, no protocolo (CLAUDE.md)
ou na estrutura. Cada pergunta é feita numa sessão nova, na raiz do projeto:

    claude -p "<pergunta>" > saida.txt

e a saída precisa conter **todos** os termos da coluna "deve citar" e
respeitar o comportamento esperado. Rodar também `docs/perguntas-teste/reforma.md`.

| # | Pergunta | Deve citar | Comportamento esperado |
|---|---|---|---|
| S1 | Uma empresa de comércio no Simples Nacional tem RBT12 de R$ 600.000,00. Qual é a alíquota efetiva? | `sn-calculo-aliquota-efetiva` | Mostra a fórmula completa (RBT12 × Aliq − PD) ÷ RBT12 com 9,50% e 13.860,00 da 3ª faixa do Anexo I e chega a ≈ 7,19% |
| S2 | Um escritório de engenharia no Simples tem folha de salários igual a 25% da receita bruta. Em qual Anexo ele é tributado? | `sn-fator-r` | Fator R < 28% → Anexo V; explica a fórmula da folha (inclui pró-labore, CPP e FGTS) |
| S3 | Uma empresa que aluga imóveis próprios pode optar pelo Simples Nacional? | `sn-vedacoes-ingresso` | Não: art. 17, XV (redação da LC 214/2025) |
| S4 | O DAS de outubro de 2026 já inclui IBS e CBS? | `sn-abrangencia-tributos` | Não: IBS e CBS entram no DAS só a partir de 01/01/2027 (LC 214, art. 517); separa claramente hoje × 2027 |
| S5 | Em 2027, uma indústria optante pelo Simples que não fabrica produto sujeito ao IPI mantido pelo ADCT continua no Anexo II? | `sn-segregacao-receitas` | Não: a partir de 01/01/2027 vai para o Anexo I; o Anexo II fica para o IPI mantido (art. 126, III, "a", do ADCT) |
| S6 | Quanto o MEI vai pagar de ICMS, ISS, IBS e CBS por mês em 2027? | `sn-mei` | R$ 1,00 de ICMS, R$ 5,00 de ISS, R$ 0,994 de CBS e R$ 0,006 de IBS, total R$ 7,00 (Anexo VII), além da contribuição previdenciária |
| S7 | Quem compra de uma empresa do Simples Nacional pode tomar crédito de IBS e CBS? | `sn-creditos` | Sim, a partir de 2027, em montante equivalente ao cobrado no regime único (art. 23, §1º-A); cruza com a nota da reforma sobre créditos |
| S8 | Se uma empresa pedir a exclusão do Simples por opção em janeiro de 2027, a partir de quando a exclusão produz efeitos? | `sn-exclusao` | Aponta que o §4º do art. 31 (efeitos no mesmo ano) é revogado em 30/11/2026; logo vale a regra geral: 1º de janeiro do ano seguinte |
| S9 | A multa do art. 38-B da LC 123 é de 60% para optantes do Simples? | `sn-acrescimos-penalidades` | Não: é **redução** das multas acessórias fixas/mínimas (MEI 90%; ME/EPP 50%, que passa a 60% em 2027) |
| S10 | A partir de quando a NFS-e de padrão nacional é obrigatória para optantes do Simples, e quais são as regras detalhadas de emissão? | `sn-obrigacoes-acessorias` | Data 01/11/2026 (Res. CGSN 191); diz que o detalhamento da Res. CGSN 140 é lacuna (fase B), sem inventar regras |
| S11 | Qual é o sublimite de ICMS adotado pelo Estado de São Paulo no Simples Nacional em 2026? | `sn-sublimites-icms-iss` | Explica a regra federal (R$ 3.600.000,00; opção de R$ 1.800.000,00 só para Estados com PIB até 1%) e sinaliza que o ato estadual está fora do escopo; não inventa |
| S12 | Qual é a parcela de IRPJ na repartição do Anexo III do Simples na 1ª faixa? | `sn-anexo-iii-servicos` | 4,00% (tabela vigente); trata como dentro do escopo (IRPJ dentro do Simples) |
