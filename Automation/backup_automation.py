#!/usr/bin/python
#coding: utf-8

import os
import shutil
import smtplib
import telegram
import time

def backup(src, dst, email, token, chat_id):
    try:
        shutil.copytree(src, dst)
        message = "Backup realizado com sucesso!"
        success = True
    except Exception as e:
        message = "Erro ao realizar backup: " + str(e)
        success = False

    if email:
        send_email(email, message, success)
    
    if token and chat_id:
        send_telegram_message(token, chat_id, message)

def send_email(to, message, success):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('seu_email@gmail.com', 'sua_senha')
    subject = "Backup realizado com sucesso!" if success else "Erro ao realizar backup"
    body = message
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail('seu_email@gmail.com', to, msg)
    server.quit()

def send_telegram_message(token, chat_id, message):
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=message)

if _name_ == "_main_":
    src = "/caminho/para/seu/diretorio/de/origem"
    dst = "/caminho/para/seu/disco/externo/ou/nuvem/diretorio/destino"
    email = "seu_email@gmail.com"
    token = "seu_token_do_telegram"
    chat_id = "seu_id_de_chat_no_telegram"
    interval = 86400 # Backup será realizado a cada 24 horas

    while True:
        backup(src, dst, email, token, chat_id)
        time.sleep(interval)
