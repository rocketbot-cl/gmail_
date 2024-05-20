



# Gmail
  
Module for performing actions in Gmail  

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


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

6. Get table data from email by ID  
Reads an email by ID and returns a list of the data from the tables in the email body

7. Reply email for ID  
Reply to an email by its ID, having the possibility to add a message body and attachments.

8. Create Label  
Create a label in Gmail, where we can move our mails having the behavior of a folder.

9. Move email to label  
Move an email to a label. We must take into account the ID of the email to move and the name of the label.

10. Mark email as unread  
Mark email as unread indicating its ID

11. Forward email for ID  
Forward email by ID. We indicate the recipient(s) to whom to forward the email and the possibility to change the subject.

12. Download attachments for ID  
Downloads email attachments and saves them in a folder

13. Close Server  
Close server connection  




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