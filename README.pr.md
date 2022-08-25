# Gmail
  
Módulo para realizar ações no Gmail 

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  


## Como usar este módulo
Para usar este módulo, teremos que fazer a seguinte configuração em nossa conta do Gmail:
1. Vá para a seção "Gerenciar Conta do Google".
2. Em seguida, iremos para a seção de "Segurança" que está no painel esquerdo.
3. Ativar a verificação em duas etapas
4. Na opção "Acesso ao Google", acesse as senhas do Aplicativo.
5. Em "Selecionar aplicativo" colocamos 'Outro' e atribuímos um nome para identificá-lo.
6. Clicamos no botão Gerar e copiamos a senha do aplicativo gerada.
7. No módulo gmail_ colocamos o email escolhido e como senha utilizamos a senha do aplicativo gerada.


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

6. Responder e-mail para ID  
Responder a um e-mail pelo seu ID, tendo a possibilidade de adicionar um corpo de mensagem e anexos.

7. Criar etiqueta  
Crie um marcador no Gmail, onde podemos mover nossos e-mails com o comportamento de uma pasta

8. Mover e-mail para etiqueta  
Mover um e-mail para uma etiqueta. Devemos levar em consideração o ID do e-mail a ser movido e o nome do rótulo

9. Marcar e-mail como não lido  
Marcar e-mail como não lido indicando seu ID

10. Fechar conexão  
Fechar conexão do servidor

11. Reenviar e-mail para ID  
Reenviar e-mail por ID. Indicamos o(s) destinatário(s) para reenviar o e-mail e a possibilidade de alterar o assunto.

12. Baixar anexos para ID  
Baixa anexos de e-mail e os salva em uma pasta  



### Changes
Wed Feb 17 13:47:47 2021  Merge branch master of https://github.com/rocketbot-cl/gmail_

Wed Sep 2 10:43:37 2020  Merge branch master of https://github.com/rocketbot-cl/gmail_

Fri Nov 15 15:36:49 2019  Merge branch master of https://github.com/rocketbot-cl/Gmail

Tue Nov 5 14:32:16 2019  Merge branch master of https://github.com/rocketbot-cl/Gmail

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