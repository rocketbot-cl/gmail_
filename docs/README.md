



# Gmail
  
Módulo para realizar acciones en Gmail  

## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## Como usar este módulo
Para usar este modulo deberemos realizar la siguiente configuracion en nuestra cuenta de Gmail:

1. Ir a la seccion de "Gestionar tu cuenta de Google"
2. Luego iremos al apartado de "Seguridad" que se encuentra en el
 panel izquierdo.
3. Dentro de esa seccion, buscamos la parte "Acceso de aplicaciones poco seguras" y le damos click en 
"Activar acceso".
4. Activamos la casilla que dice "Permitir el acceso de aplicaciones poco seguras". Tambien podemos acceder directamente desde el siguiente link https://myaccount.google.com/lesssecureapps


## Overview


1. Server Configuration  
With this command we enable the execution of other commands, configuring the server with our mail and password.

2. Send Email  
Send email, before you must configurate the server

3. List all emails  
List all email, you can specify a filter

4. List unread emails  
List all unread emails, you can specify a filter

5. Read email for ID  
Reads an email by ID and gets all email data, the message body and its attachments

6. Reply email for ID  
Reply to an email by its ID, having the possibility to add a message body and attachments.

7. Create Label  
Create a label in Gmail, where we can move our mails having the behavior of a folder.

8. Move email to label  
Move an email to a label. We must take into account the ID of the email to move and the name of the label.

9. Mark email as unread  
Mark email as unread indicating its ID

10. Close Server  
Close server connection

11. Forward email for ID  
Forward email by ID. We indicate the recipient(s) to whom to forward the email and the possibility to change the 
subject.  



### Updates
## 21-Dic-2021
- Add label to unseen mails
## 02-Sep-2021
- New command: Forward email.

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