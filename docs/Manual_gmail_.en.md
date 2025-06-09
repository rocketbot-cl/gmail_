



# Gmail
  
Module for performing actions in Gmail  

*Read this in other languages: [English](Manual_gmail_.md), [Português](Manual_gmail_.pr.md), [Español](Manual_gmail_.es.md)*
  
![banner](imgs/Banner_gmail_.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## Como usar este módulo

Para usar este modulo debemos realizar la siguiente configuracion en nuestra cuenta de Gmail:
1. Ir a la seccion de "Gestionar tu cuenta de Google"
2. Luego iremos al apartado de "Seguridad" que se encuentra en el panel izquierdo.
3. Activar verificación en dos pasos
4. En la opción "Acceso a Google" acceder a Contraseñas de aplicaciones.
5. En "Seleccionar aplicación" colocamos 'Otro' y le asignamos un nombre para identificarla.
6. Hacemos click en el botón Generar y copiamos la contraseña de aplicación generada.
7. En el módulo gmail_ colocamos el email elegido y como contraseña se utiliza la contraseña de aplicación generada.

Documentación para generar contraseña de aplicación: https://docs.rocketbot.com/2024/08/07/crear-contrasena-de-aplicacion-para-gmail/


## Description of the commands

### Server Configuration
  
With this command we enable the execution of other commands, configuring the server with our mail and password.
|Parameters|Description|example|
| --- | --- | --- |
|User|Email to use|user@example.com|
|Password|Password of the email or application password|******|
|Conexión SSL|Enable SSL connection|True|
|Assign result to a Variable|Name of the variable where the result will be stored without {}|Variable|

### Send Email
  
Send email, before you must configurate the server
|Parameters|Description|example|
| --- | --- | --- |
|From|Optional. Indicate the name of the sender of the email|Test|
|To|Indicate the recipient, for multiple recipients, comma separated|to@mail.com, to2@mail.com|
|Cc|Indicate who to send a copy to, for multiple recipients, comma separated|cc@mail.com, cc2@mail.com|
|Bcc|Select to send a hidden copy|bcc@mail.com, bcc2@mail.com|
|Subject|Indicate the subject of the email|This is a test email|
|Body|Indicate the body of the email|Hi from Rocketbot!|
|Attached File|Select a file to attach|C:/User/Desktop/test.txt|
|Folder (Multiple files)|Select a folder to attach multiple files|C:/User/Desktop/Files|

### List all emails
  
List all email, you can specify a filter
|Parameters|Description|example|
| --- | --- | --- |
|Filter|Filter of mail. After the filter, you must place the search parameter in double quotes. Leave empty to get them all|SUBJECT "Example text"|
|Folder|Folder of mail. Empty for get only INBOX|Folder|
|Assign to variable|Name of the variable where the result will be stored|Variable|

### List unread emails
  
List all unread emails, you can specify a filter
|Parameters|Description|example|
| --- | --- | --- |
|Filter|Filter to apply to unread emails. After the filter, the search parameter must be placed in double quotes. Leave empty to bring all unread.|SUBJECT "Example text"|
|Label|Folder name where read the mail. If it's not a native gmail label, type the name with quot marks|[Gmail]/All|
|Assign to variable|Variable where the unread emails will be saved.|Variable|

### Read email for ID
  
Reads an email by ID and gets all email data, the message body and its attachments
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to read|345|
|Label|Folder name where read the mail. If it's not a native gmail label, type the name with quot marks|[Gmail]/All|
|Assign to variable|Variable name where save the email|Variable|
|Path for download attachment|Path where save the attachments|C:/User/Desktop|

### Get table data from email by ID
  
Reads an email by ID and returns a list of the data from the tables in the email body
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to read|345|
|Assign to variable|Variable name where save the list of table data|Variable|

### Reply email for ID
  
Reply to an email by its ID, having the possibility to add a message body and attachments.
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to reply|355|
|Folder|Folder of mail. Empty for get only INBOX|Folder|
|Body|Message to forward|This is a test response|
|Attached File|Attached file to forward|C:/User/Desktop/test.txt|

### Create Label
  
Create a label in Gmail, where we can move our mails having the behavior of a folder.
|Parameters|Description|example|
| --- | --- | --- |
|Label Name|Name of the label to create|test_label|

### Move email to label
  
Move an email to a label. We must take into account the ID of the email to move and the name of the label.
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID that will be moved to another label|345|
|Label Name|Label name to which the email will be moved|test|
|Assign result to variable|Name of the variable to which the result will be assigned|Variable|

### Mark email as unread
  
Mark email as unread indicating its ID
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|ID of the email to mark as unread|345|
|Folder|Folder of mail. Empty for get only INBOX|Folder|

### Forward email for ID
  
Forward email by ID. We indicate the recipient(s) to whom to forward the email and the possibility to change the subject.
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|ID of the email to be forwarded|355|
|Email|Destination email|test@email.com|

### Download attachments for ID
  
Downloads email attachments and saves them in a folder
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to read|345|
|Label|Folder name where read the mail. If it's not a native gmail label, type the name with quot marks|[Gmail]/All|
|Extensions|Extensions of the files to download. Separate by commas|pdf,jpg,xslx|
|Path for download attachment|Path where save the attachments|C:/User/Desktop|

### Close Server
  
Close server connection
|Parameters|Description|example|
| --- | --- | --- |
