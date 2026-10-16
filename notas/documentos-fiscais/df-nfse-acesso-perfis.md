---
título: NFS-e Nacional — acesso ao emissor (usuário/senha, certificado digital, GOV.BR) e níveis de acesso
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seções 1.1 e 10 (p. 7-15 e 118-125); NT 2025.002-RTC v1.52 (referência de hierarquia, ver df-visao-geral-reforma-nfe)
vigencia: atual
texto-base: 2026-10-16
---

# NFS-e Nacional: como entrar no emissor

## A lógica em uma frase

Há **três portas** para o Emissor Web: **usuário e senha** (exige um cadastro de
"primeiro acesso" que usa dados da Receita como prova de identidade),
**certificado digital** e **GOV.BR** (este, por ora, só para MEI). Quem não consegue
a senha pelo autoatendimento cai no **atendimento presencial do município**.

## As três formas de acesso

| Forma | Quem pode | Observações do guia |
|---|---|---|
| **Usuário/senha** (CPF ou CNPJ + senha) | PF e PJ | Exige o cadastro de "Fazer primeiro acesso". Funciona também para o MEI. |
| **Certificado digital** | PF e PJ | O certificado **A1**, instalado no computador, não pede senha ao ser usado. Dá acesso às consultas e à emissão. |
| **GOV.BR** | **Só MEI** (por ora) | Aceita os níveis **prata e ouro**; o **bronze** é considerado insuficiente. |

### GOV.BR (item 10.6.3)

- A princípio, a forma é permitida **apenas para MEI**. Prestadores que não são MEI
  (PF por CPF ou PJ por CNPJ) continuam com login e senha; o acesso GOV.BR deles
  "será tratado em uma nova pré-especificação".
- O representante legal do MEI entra por GOV.BR e há **vinculação automática** do
  CPF dele ao CNPJ MEI.
- Qualquer forma de entrada no GOV.BR serve (login e senha, certificado, certificado
  em nuvem, login com banco, QR Code), desde que o nível seja prata ou ouro.
- O MEI **não precisa assinar** as notas com certificado digital.
- O login e senha do próprio sistema continua valendo para o MEI (com o "primeiro
  acesso").

## Primeiro acesso por usuário e senha (item 1.1.1 e 10.3)

O cadastro é feito **pelo próprio usuário** no Portal Nacional NFS-e.

**Pessoa física:** CPF + data de nascimento → número do **título de eleitor** →
números dos **recibos das declarações do IRPF** (dos dois últimos anos "se for o
caso") → e-mail e senha → **código de segurança** enviado ao e-mail.

**Pessoa jurídica:** CNPJ + CPF do **responsável** + data de nascimento do
responsável → título de eleitor do responsável → recibos do IRPF do responsável →
e-mail e senha → código de segurança por e-mail. Os dados verificados são os do
**CPF responsável legal pelo CNPJ**.

Regras do item 10.3 sobre os recibos do IRPF:

- Informam-se os recibos das declarações **ativas** (últimas entregues) de que o CPF
  é titular.
- Se só um dos dois últimos exercícios tem declaração, é obrigatório informar o
  recibo da declaração ativa **do ano**.
- **Sem nenhum recibo**, usa-se o **título de eleitor**, obtido do cadastro CPF da
  RFB.
- **Sem título de eleitor**, não é possível criar usuário e senha: a pessoa é
  orientada a comparecer ao município onde é emitente, ou a usar o **certificado
  digital**, que dispensa o comparecimento.

### Mensagens de erro do cadastro

| Situação | Mensagem do guia |
|---|---|
| CPF não existe | "Não foi possível recuperar informações do Contribuinte." |
| CPF inválido (dígito verificador) | "Informe um CPF válido" |
| Data de nascimento diferente da do cadastro CPF | "A data de nascimento informada não corresponde ao CPF informado." |
| CNPJ não existe | "Não foi possível recuperar informações do Contribuinte." |
| CPF do responsável diferente do Cadastro CNPJ | "O CPF informado não corresponde ao CPF responsável pelo CNPJ informado." |

## Recuperar a senha (item 10.4)

Segue quase o mesmo fluxo do primeiro acesso, mas o usuário já cadastrado pode
acionar a recuperação desde o início. Se o CPF/CNPJ não for encontrado, o sistema
oferece entrar com um CPF/CNPJ reconhecido ou fazer o primeiro acesso. Se for
encontrado, o sistema **lista os e-mails cadastrados** para o usuário escolher para
qual enviar o link de redefinição. A existência do CPF/CNPJ, os recibos do IRPF e o
título de eleitor são conferidos nos cadastros da RFB. O processo fica registrado na
tabela de log.

## Níveis de acesso (item 10.1)

| Nível | Forma de acesso |
|---|---|
| 1 | usuário/senha |
| 2 | usuário/senha com **validação e cadastro prévio presencial** pelo município do emitente |
| 3 | certificado digital |

O acesso por usuário/senha libera as funcionalidades do nível correspondente, sem
certificado. Se o emitente estiver **cadastrado mas bloqueado** para emissão no CNC,
o sistema deixa abrir a tela de emissão, mas **avisa por mensagem** a situação de
bloqueio.

## Cadastro presencial (item 10.5)

O **cadastro inicial** de autorização para emitir NFS-e e a **regularização** da
situação cadastral são feitos no atendimento presencial do município do emitente. O
Gestor Atendente Municipal confere a documentação que o município exige e cadastra
ou regulariza o emitente no CNC NFS-e, pelo Painel Administrativo Municipal. O
emitente define uma senha e, no primeiro acesso, o sistema pede que ela seja trocada.
A documentação exigida é **definida por cada município** e não consta do guia.

## Ligações

- [[df-nfse-visao-geral]]: o que é o emissor e os canais.
- [[df-nfse-painel-configuracoes]]: o que fazer logo após entrar.
- [[sn-mei-regulamentacao]]: o MEI e a NFS-e nacional.
