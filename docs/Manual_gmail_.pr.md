



# Gmail
  
Módulo para realizar acciones no Gmail  

*Read this in other languages: [English](Manual_gmail_.md), [Português](Manual_gmail_.pr.md), [Español](Manual_gmail_.es.md)*
  
![banner](imgs/Banner_gmail_.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Configuração do servidor
  
Com este comando habilitamos a execução de outros comandos, configurando o servidor com nosso email e senha
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuário|E-mail para usar|user@example.com|
|Senha|Senha do e-mail ou senha do aplicativo|******|
|Conexão SSL|Ativar conexão SSL|True|
|Atribuir resultado a uma variável|Nome da variável onde o resultado será armazenado sem {}|Variável|

### Enviar email
  
Envie um email, você deve configurar previamente o servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|De|Opcional. Indique o nome do remetente do e-mail|Test|
|Para|Indique o destinatário, para vários destinatários, separados por vírgula|to@mail.com, to2@mail.com|
|Cc|Indique para quem enviar uma cópia, para vários destinatários, separados por vírgula|cc@mail.com, cc2@mail.com|
|Bcc|Selecione para enviar uma cópia oculta|bcc@mail.com, bcc2@mail.com|
|Assunto|Indique o assunto do e-mail|This is a test email|
|Mensagem|Indique o corpo do e-mail|Hi from Rocketbot!|
|Arquivo anexo|Selecione um arquivo para anexar|C:/User/Desktop/test.txt|
|Pasta (vários arquivos)|Selecione uma pasta para anexar vários arquivos|C:/User/Desktop/Files|

### Listar todos os e-mails
  
Listar todos os e-mails, você pode especificar um filtro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Filtro de correio. Depois do filtro, você deve colocar o parâmetro de pesquisa em aspas duplas. Deixe vazio para obter todos|SUBJECT "Example text"|
|Pasta|Pasta de correio. Vazio para obter apenas INBOX|Pasta|
|Atribuir à variável|Nome da variável onde o resultado será armazenado|Variável|

### Listar e-mails não lidos
  
Liste todos os emails não lidos, você pode especificar um filtro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Filtro a ser aplicado aos e-mails não lidos. Depois do filtro, o parâmetro de pesquisa deve ser colocado entre aspas duplas. Deixe vazio para obter todos os não lidos.|SUBJECT "Example text"|
|Label|Nome do label onde fica o mail. Se não for um label de gmail nativo, digite o nome com vírgulas invertidas|[Gmail]/All|
|Atribuir à variável|Variável onde os emails não lidos serão salvos|Variável|

### Ler e-mail por ID
  
Lê um email por ID e obtém todos os dados do email, o corpo da mensagem e seus anexos
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID de e-mail para ler|345|
|Label|Nome do label onde fica o mail. Se não for um label de gmail nativo, digite o nome com vírgulas invertidas|[Gmail]/All|
|Atribuir à variável|Nome da variável onde salvar o e-mail|Variável|
|Caminho para download do anexo|Caminho onde salvar os anexos|C:/User/Desktop|

### Obter dados da tabela do e-mail por ID
  
Lê um e-mail por ID e retorna uma lista dos dados das tabelas do corpo do e-mail
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID de e-mail para ler|345|
|Atribuir à variável|Nome da variável onde salvar a lista de dados da tabela|Variável|

### Responder e-mail para ID
  
Responder a um e-mail pelo seu ID, tendo a possibilidade de adicionar um corpo de mensagem e anexos.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID de e-mail para responder|355|
|Pasta|Pasta de correio. Vazio para obter apenas INBOX|Pasta|
|Body|Mensagem para reenviar|This is a test response|
|Arquivo anexo|Arquivo anexado para reenviar|C:/User/Desktop/test.txt|

### Criar etiqueta
  
Crie um marcador no Gmail, onde podemos mover nossos e-mails com o comportamento de uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da etiqueta|Nome da etiqueta a ser criada|test_label|

### Mover e-mail para etiqueta
  
Mover um e-mail para uma etiqueta. Devemos levar em consideração o ID do e-mail a ser movido e o nome do rótulo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID de e-mail que será movido para outra etiqueta|345|
|Nome da etiqueta|Nome da etiqueta para o qual o e-mail será movido|test|
|Atribuir resultado à variável|Nome da variável à qual o resultado será atribuído|Variável|

### Marcar e-mail como não lido
  
Marcar e-mail como não lido indicando seu ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID do e-mail a ser marcado como não lido|345|

### Reenviar e-mail para ID
  
Reenviar e-mail por ID. Indicamos o(s) destinatário(s) para reenviar o e-mail e a possibilidade de alterar o assunto.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID do e-mail a ser reenviado|355|
|Email|Email de destino|test@email.com|

### Baixar anexos para ID
  
Baixa anexos de e-mail e os salva em uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email ID|ID de e-mail para ler|345|
|Label|Nome do label onde fica o mail. Se não for um label de gmail nativo, digite o nome com vírgulas invertidas|[Gmail]/All|
|Extensões|Extensões dos arquivos para baixar. Separe por vírgulas|pdf,jpg,xslx|
|Caminho para download do anexo|Caminho onde salvar os anexos|C:/User/Desktop|

### Fechar conexão
  
Fechar conexão do servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
