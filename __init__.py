# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import base64
import email
import imaplib
import os
import re
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid, parsedate_to_datetime
from textwrap import dedent
from typing import Union

from bs4 import BeautifulSoup

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'gmail_' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from mailparser import mailparser
from mail_common import Mail

global gmail_module
global fromaddr
global server
global password
global mail
global id_

def is_html(text):
    from bs4 import BeautifulSoup
    return bool(BeautifulSoup(text, "html.parser").find())

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

class Gmail_(Mail):
            def __init__(self, user, pwd, timeout):
                super().__init__(user, pwd, timeout,
                                        smtp_host='smtp.gmail.com', smtp_port=587,
                                        imap_host='imap.gmail.com', imap_port=993)
            
            def connect_imap(self):
                try:
                    self.imap = imaplib.IMAP4_SSL(self.imap_host, 993)
                except:
                    self.imap = imaplib.IMAP4(self.imap_host, 465)

                self.imap.login(self.user, self.pwd)
                return self.imap

def parse_uid(tmp):
    pattern_uid = re.compile(r'\d+ \(UID (?P<uid>\d+)\)')
    try:
        tmp = tmp.decode()
    except:
        pass
    match = pattern_uid.match(tmp)
    return match.group('uid')


if module == "conf_mail":

    conx = ""

    try:
        fromaddr = GetParams('from')
        password = GetParams('password')
        ssl = GetParams('ssl')
        var_ = GetParams('var_')

        if ssl is not None:
            ssl = eval(ssl)

        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)

        if ssl:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
        server.login(fromaddr, password)
        gmail_module = Gmail_(fromaddr, password, 99)
        conx = True

    except:
        PrintException()
        conx = False

    SetVar(var_, conx)

if module == "send_mail":
    to = GetParams('to')
    subject = GetParams('subject')
    body_ = GetParams('body')
    cc = GetParams('cc')
    bcc = GetParams('bcc')
    attached_file = GetParams('attached_file')
    files = GetParams('attached_folder')
    from_name = GetParams('from_name')
    filenames = []

    try:
        # msg = MIMEMultipart()
        # msg['From'] = fromaddr
        # msg['To'] = to
        # msg['Cc'] = cc
        # msg['Subject'] = subject

        # if cc:
        #     toAddress = to.split(",") + cc.split(",")
        # if bcc:
        #     toAddress = to.split(",") + bcc.split(",")
        # elif not cc and not bcc:
        #     toAddress = to.split(",")


        # if not body_:
        #     body_ = ""
        # body = body_.replace("\n", "<br/>")
        
        # if not "src" in body:
        #     msg.attach(MIMEText(body, 'html'))

        # for match in get_regex_group(r"src=\"(.*)\"", body):
        #     path = match[0]
            
        #     if path.startswith(("http", "https")):
        #         msg.attach(MIMEText(body, 'html'))
        #         continue

        #     image_cid = make_msgid()
        #     body = body.replace(path, "cid:" + image_cid[1:-1])

        #     msg.attach(MIMEText(body, 'html'))
            
        #     img_ = open(path, 'rb')
        #     image = MIMEImage(img_.read())
        #     img_.close()
        #     image.add_header('Content-ID', image_cid)
        #     image.add_header('Content-Disposition', 'inline', filename=os.path.basename(path))
        #     image.add_header("Content-Transfer-Encoding", "base64")
        #     msg.attach(image)

        # if files:
        #     for f in os.listdir(files):
        #         f = os.path.join(files, f)
        #         filenames.append(f)

        #     if filenames:
        #         for file in filenames:
        #             filename = os.path.basename(file)
        #             attachment = open(file, "rb")
        #             part = MIMEBase('application', 'octet-stream')
        #             part.set_payload((attachment).read())
        #             attachment.close()
        #             encoders.encode_base64(part)
        #             part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        #             msg.attach(part)

        # else:
        #     if attached_file:
        #         if os.path.exists(attached_file):
        #             filename = os.path.basename(attached_file)
        #             attachment = open(attached_file, "rb")
        #             part = MIMEBase('application', 'octet-stream')
        #             part.set_payload((attachment).read())
        #             attachment.close()
        #             encoders.encode_base64(part)
        #             part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        #             msg.attach(part)

        # text = msg.as_string()
        # server.sendmail(fromaddr, toAddress, text)
        # # server.close()

        type_ = 'multipart'

        if cc is None:
            cc = ""
        if bcc is None:
            bcc = ""
        if attached_file is None:
            attached_file = ""
        if files is None:
            files = ""
        if from_name is None:
            from_name = ""

        body_ = body_.replace(r"\n", "<br/>") if body_ else ""

        if is_html(body_):
            gmail_module.send_mail_html(
                to,
                subject,
                cc=cc,
                bcc=bcc,
                attachments_path=[attached_file, files],
                type_=type_,
                body=body_,
                from_name=from_name
            )
        else:
            gmail_module.send_mail(
                to,
                subject,
                cc=cc,
                bcc=bcc,
                attachments_path=[attached_file, files],
                type_=type_,
                body=body_,
                from_name=from_name
            )

    except Exception as e:
        PrintException()
        raise e

if module == "get_mail":
    filtro = GetParams('filtro')
    folder = GetParams('folder')
    var_ = GetParams('var_')
    

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        if folder is None:
            mail.select("inbox")  # connect to inbox.
        if folder:
            from imapclient import imap_utf7
            folder = imap_utf7.encode(folder)
            mail.select(folder)
        
        if filtro and len(filtro) > 0:
            filtro = '(' + filtro + ')'
            result, data = mail.search(None, filtro, "ALL")
        else:
            result, data = mail.search(None, "ALL")

        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string


        lista = [b.decode() for b in id_list]

        SetVar(var_, lista)
    except Exception as e:
        PrintException()
        raise e
    
if module == "get_tables":
    id_ = GetParams('id_')
    var_ = GetParams('var_')

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        mail.login(fromaddr, password)
        mail.select('INBOX')

        # mail.select()
        typ, data = mail.fetch(id_, '(RFC822)')
        raw_email = data[0][1]
        # converts byte literal to string removing b''
        try:
            raw_email_string = raw_email.decode('utf-8')
        except UnicodeDecodeError:
            raw_email_string = raw_email.decode('latin1')

        email_message = email.message_from_string(raw_email_string)

        mail_ = mailparser.parse_from_string(raw_email_string)

        
        bs_mail = BeautifulSoup(mail_.body, 'html.parser')
        tables = []
        for tab in bs_mail.find_all("table"):
            table = []
            for tr in tab.find_all("tr"):
                td = tr.find_all("td")
                for tr in td:
                    row = tr.text

                    row = row.replace("\xa0", "").replace("\n", " ").replace("\r", "").replace("\t", "")

                    table.append(row)
            tables.append(table)
  
        if len(tables) == 0:
            tables = None
        elif len(tables) == 1:
            tables = tables[0]

        SetVar(var_, tables)

    except Exception as e:
        PrintException()
        raise e


    

if module == "get_unread":
    
    filtro = GetParams('filtro')
    var_ = GetParams('var_')
    folder = GetParams('folder')
    
    if filtro and len(filtro) > 0:
        filtro = '(' + filtro + ')'
    
    try:
        
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)

        mail.list()


        # Out: list of "folders" aka labels in gmail.
        if folder is None:
            mail.select("inbox")  # connect to inbox.
        if folder:
            from imapclient import imap_utf7
            folder = imap_utf7.encode(folder)
            mail.select(folder)



        if filtro and len(filtro) > 0:
            result, data = mail.search(None, filtro, "UNSEEN")
        else:
            result, data = mail.search(None, "UNSEEN")

        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string

        # print('ID',id_list)
        lista = [b.decode() for b in id_list]

        SetVar(var_, lista)
    except Exception as e:
        PrintException()
        raise e

if module == "read_mail":
    id_ = GetParams('id_')
    var_ = GetParams('var_')
    att_folder = GetParams('att_folder')
    folder = GetParams('folder')

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        if not folder:
            folder = "inbox"

        if folder:
            from imapclient import imap_utf7
            folder = imap_utf7.encode(folder)
       
        mail.login(fromaddr, password)
        mail.select(folder)

        # mail.select()
        typ, data = mail.fetch(id_, '(RFC822)')
        raw_email = data[0][1]
        # converts byte literal to string removing b''
        try:
            raw_email_string = raw_email.decode('utf-8')
        except:
            raw_email_string = raw_email.decode('latin1')
        email_message = email.message_from_string(raw_email_string)
        
        mail_ = mailparser.parse_from_string(raw_email_string)

        links = []
        try:
            bs = ""
            bs_mail = BeautifulSoup(mail_.body, 'html.parser')
            try:
                bs = bs_mail.body.get_text()
            except:
                bs = mail_.body

            links = [{a.get_text(): a["href"] for a in bs_mail.find_all("a")}]

        except:
            bs = mail_.body

        if "--- mail_boundary ---" in bs.__str__():
            html_list = bs.split("--- mail_boundary ---")
            html = BeautifulSoup(html_list[1], 'html.parser').get_text()
            html_list[1] = html
            bs = "\n".join(html_list)

        nameFile = []

        for att in mail_.attachments:
            name_ = att['filename']
            name_ = name_.replace("\r\n", '')
            nameFile.append(name_)

            fileb = att['payload']

            if att_folder:
                try:
                    from xml.etree import ElementTree as ET

                    tmp_xml = ET.fromstring(fileb)
                    with open(os.path.join(att_folder, name_), 'w') as file_:
                        file_.write(fileb)
                        file_.close()
                except:
                    cont = base64.b64decode(fileb)
                    with open(os.path.join(att_folder, name_), 'wb') as file_:
                        file_.write(cont)
                        file_.close()

        def fix_date_timezone(date:Union[str, datetime.datetime], timezone:Union[str, int]=""):
            from email.utils import parsedate_to_datetime
            from datetime import timedelta
            from time import gmtime, strftime
            """Fix the date timezone."""
            try:
                local_timezone = strftime("%z", gmtime())[:3]
                if isinstance(date, str):
                    date = parsedate_to_datetime(date)
                if not timezone:
                    timezone = date.tzname().replace('UTC','').replace('00:', '')
                if not timezone:
                    timezone = 0
                if int(timezone) > int(local_timezone):
                    date = date - timedelta(hours=abs(int(local_timezone)))
                if int(timezone) < int(local_timezone):
                    date = date + timedelta(hours=abs(int(timezone)-int(local_timezone)))
                
                return date.strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                PrintException()

            return date.strftime('%d/%m/%Y - %H:%M:%S')
        
        timezone_mail = mail_.timezone
        final = {"date": fix_date_timezone(email_message['Date'], timezone_mail), 'subject': mail_.subject,
                 'from': ", ".join([b for (a, b) in mail_.from_]),
                 'to': ", ".join([b for (a, b) in mail_.to]), 'cc': ", ".join([b for (a, b) in mail_.cc]), 'body': bs,
                 'files': nameFile, 'links': links}
        SetVar(var_, final)
    except Exception as e:
        PrintException()
        raise e



if module == "reply_email":
    id_ = GetParams('id_')
    folder = GetParams('folder')
    body_ = GetParams('body')
    attached_file = GetParams('attached_file')
    # print(body_, attached_file)

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        if folder is None:
            mail.select("inbox")  # connect to inbox.
        if folder:
            from imapclient import imap_utf7
            folder = imap_utf7.encode(folder)
            mail.select(folder)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)

        # mail.select()
        typ, data = mail.fetch(id_, '(RFC822)')
        raw_email = data[0][1]
        mm = email.message_from_bytes(raw_email)

        # msg = MIMEMultipart()
        # msg.attach(MIMEText(body_, 'plain'))

        #    m_ = create_auto_reply(mm, body_)
        mail__ = MIMEMultipart()
        mail__['Message-ID'] = make_msgid()
        mail__['References'] = mail__['In-Reply-To'] = mm['Message-ID']
        mail__['Subject'] = 'Re: ' + mm['Subject']
        mail__['From'] = mm['To'] = mm['Reply-To'] or mm['From']
        mail__.attach(MIMEText(dedent(body_), 'html'))

        if attached_file:
            if os.path.exists(attached_file):
                filename = os.path.basename(attached_file)
                attachment = open(attached_file, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                attachment.close()
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                mail__.attach(part)

        # print("FROMADDR",fromaddr, "FROM",mm['From'], "TO:",mm['To'])
        server.sendmail(fromaddr, mm['From'], mail__.as_bytes())
        # server.sendmail(fromaddr, mm['To'], mail__.as_bytes())
        # server.close()
        mail.logout()
    except Exception as e:
        PrintException()
        raise e

if module == "create_folder":
    try:
        folder_name = GetParams('folder_name')
        host = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(host)
        mail.login(fromaddr, password)
        mail.create(folder_name)
    except Exception as e:
        PrintException()
        raise e

if module == "move_mail":
    # imap = GetGlobals('email')
    id_ = GetParams("id_")
    label_ = GetParams("label_")
    var = GetParams("var")

    if not id_:
        raise Exception("No ha ingresado ID de email a mover")
    if not label_:
        raise Exception("No ha ingresado carpeta de destino")
    try:
        # login on IMAP server
        # if imap.IMAP_SSL:
        #     mail = imaplib.IMAP4_SSL('imap.gmail.com')
        # else:
        #     mail = imaplib.IMAP4('imap.gmail.com')

        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.select('inbox', readonly=False)
        resp, data = mail.fetch(id_, "(UID)")
        msg_uid = parse_uid(data[0])

        result = mail.uid('COPY', str(int(msg_uid)), label_)

        if result[0] == 'OK':
            mov, data = mail.uid('STORE', msg_uid, '+FLAGS', r'(\Deleted)')
            res = mail.expunge()
            if var:
                ret = True if res[0] == 'OK' else False
                SetVar(var, ret)
        else:
            raise Exception(result)
    except Exception as e:
        PrintException()
        raise e

if module == "markAsUnread":
    id_ = GetParams("id_")
    var = GetParams("var")

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.select('inbox', readonly=False)
        resp, data = mail.fetch(id_, "(UID)")
        msg_uid = parse_uid(data[0])

        data = mail.uid('STORE', msg_uid, '-FLAGS', r'(\Seen)')
    except Exception as e:
        PrintException()
        raise e


if module == "forward":
    id_ = GetParams('id_')
    to_ = GetParams('email')
    try:
        from shutil import rmtree

        temp_folder = cur_path + "temp"
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder)
        gmail_module.forward_email(id_, "inbox", temp_folder, to_)
        rmtree(temp_folder)
    except Exception as e:
        PrintException()
        raise e

if module == "get_attachments":
    id_ = GetParams('id_')
    att_folder = GetParams('att_folder')
    folder = GetParams('folder')
    extensions = GetParams('extensions')
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        if not folder:
            folder = "inbox"

        if folder:
            from imapclient import imap_utf7
            folder = imap_utf7.encode(folder)

        mail.login(fromaddr, password)
        mail.select(folder)
        typ, data = mail.fetch(id_, '(RFC822)')
        raw_email = data[0][1]
        try:
            raw_email_string = raw_email.decode('utf-8')
        except:
            raw_email_string = raw_email.decode('latin1')
        
        mail_ = mailparser.parse_from_string(raw_email_string)
        nameFile = []
        for att in mail_.attachments:
            if extensions == "" or extensions == None:
                name_ = att['filename']
                name_ = name_.replace("\r\n", '')
                nameFile.append(name_)
                fileb = att['payload']
            else:
                ext = extensions.split(",")
                if att['filename'].split(".")[-1] in ext:
                    name_ = att['filename']
                    name_ = name_.replace("\r\n", '')
                    nameFile.append(name_)
                    fileb = att['payload']  
            if att_folder:
                try:
                    from xml.etree import ElementTree as ET

                    tmp_xml = ET.fromstring(fileb)
                    with open(os.path.join(att_folder, name_), 'w') as file_:
                        file_.write(fileb)
                        file_.close()
                except:
                    cont = base64.b64decode(fileb)
                    with open(os.path.join(att_folder, name_), 'wb') as file_:
                        file_.write(cont)
                        file_.close()
    except Exception as e:
        PrintException()
        raise e
