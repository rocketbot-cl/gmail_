# Gmail
  
Module to perform actions in Gmail
  
*Read this in other languages: [English](Manual_gmail_.md), [Portugues](Manual_gmail_.pr.md), [Español](Manual_gmail_.es.md).*
  
![banner](imgs/Banner_gmail_.png)

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module
To use this module we will have to make the following configuration in our Gmail account:
1. Go to the "Manage your Google Account" section.
2. Then we will go to the section of "Security" that is in the left panel.
3. Activate two-step verification
4. In the "Access to Google" option, access Application passwords.
5. In "Select application" we place 'Other' and assign it a name to identify it.
6. We click on the Generate button and copy the generated application password.
7. In the gmail_ module we place the chosen email and as password we use the generated application password.


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

### Reply email for ID
  
Reply to an email by its ID, having the possibility to add a message body and attachments.
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to reply|355|
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

### Close Server
  
Close server connection
|Parameters|Description|example|
| --- | --- | --- |
| --- | --- | --- |

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
|Path for download attachment|Path where save the attachments|C:/User/Desktop|
