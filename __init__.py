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
from email.utils import make_msgid
from textwrap import dedent

from bs4 import BeautifulSoup

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'gmail_' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
print(cur_path)

from mailparser import mailparser

global fromaddr
global server
global password
global mail
global id_

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")


def parse_uid(tmp):
    pattern_uid = re.compile('\d+ \(UID (?P<uid>\d+)\)')
    print('tmp', tmp)
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
            server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
        server.login(fromaddr, password)
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
    filenames = []

    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = to
        msg['Cc'] = cc
        msg['Subject'] = subject

        if cc:
            toAddress = to.split(",") + cc.split(",")
        if bcc:
            toAddress = to.split(",") + bcc.split(",")
        elif not cc and not bcc:
            toAddress = to.split(",")


        if not body_:
            body_ = ""
        body = body_.replace("\n", "<br/>")
        msg.attach(MIMEText(body, 'html'))

        if files:
            for f in os.listdir(files):
                f = os.path.join(files, f)
                filenames.append(f)

            if filenames:
                for file in filenames:
                    filename = os.path.basename(file)
                    attachment = open(file, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)

        else:
            if attached_file:
                if os.path.exists(attached_file):
                    filename = os.path.basename(attached_file)
                    attachment = open(attached_file, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)

        text = msg.as_string()
        server.sendmail(fromaddr, toAddress, text)
        # server.close()


    except Exception as e:
        PrintException()
        raise e

if module == "get_mail":
    filtro = GetParams('filtro')
    var_ = GetParams('var_')

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        mail.select("inbox")  # connect to inbox.

        if filtro and len(filtro) > 0:
            result, data = mail.search(None, filtro, "ALL")
        else:
            result, data = mail.search(None, "ALL")

        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string

        print('ID', id_list)

        lista = [b.decode() for b in id_list]

        SetVar(var_, lista)
    except Exception as e:
        PrintException()
        raise e

if module == "get_unread":
    filtro = GetParams('filtro')
    var_ = GetParams('var_')

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        mail.select("inbox")  # connect to inbox.

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

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.select("inbox")

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
            print(links)

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

        final = {"date": mail_.date.__str__(), 'subject': mail_.subject,
                 'from': ", ".join([b for (a, b) in mail_.from_]),
                 'to': ", ".join([b for (a, b) in mail_.to]), 'cc': ", ".join([b for (a, b) in mail_.cc]), 'body': bs,
                 'files': nameFile, 'links': links}

        SetVar(var_, final)
    except Exception as e:
        PrintException()
        raise e



if module == "reply_email":
    id_ = GetParams('id_')
    body_ = GetParams('body')
    attached_file = GetParams('attached_file')
    # print(body_, attached_file)

    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(fromaddr, password)
        mail.select("inbox")
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
    except:
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
            mov, data = mail.uid('STORE', msg_uid, '+FLAGS', '(\Deleted)')
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

        data = mail.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
    except Exception as e:
        PrintException()
        raise e

if module == "close":
    server.close()
