



# Gmail
  
Módulo para realizar acciones no Gmail  

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Configuração do servidor  
Com este comando habilitamos a execução de outros comandos, configurando o servidor com nosso email e senha

2. Enviar email  
Envie um email, você deve configurar previamente o servidor

3. Listar todos os e-mails  
Listar todos os e-mails, você pode especificar um filtro

4. Listar e-mails não lidos  
Liste todos os emails não lidos, você pode especificar um filtro

5. Ler e-mail por ID  
Lê um email por ID e obtém todos os dados do email, o corpo da mensagem e seus anexos

6. Obter dados da tabela do e-mail por ID  
Lê um e-mail por ID e retorna uma lista dos dados das tabelas do corpo do e-mail

7. Responder e-mail para ID  
Responder a um e-mail pelo seu ID, tendo a possibilidade de adicionar um corpo de mensagem e anexos.

8. Criar etiqueta  
Crie um marcador no Gmail, onde podemos mover nossos e-mails com o comportamento de uma pasta

9. Mover e-mail para etiqueta  
Mover um e-mail para uma etiqueta. Devemos levar em consideração o ID do e-mail a ser movido e o nome do rótulo

10. Marcar e-mail como não lido  
Marcar e-mail como não lido indicando seu ID

11. Reenviar e-mail para ID  
Reenviar e-mail por ID. Indicamos o(s) destinatário(s) para reenviar o e-mail e a possibilidade de alterar o assunto.

12. Baixar anexos para ID  
Baixa anexos de e-mail e os salva em uma pasta

13. Fechar conexão  
Fechar conexão do servidor  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**mail-parser**](https://pypi.org/project/mail-parser/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)