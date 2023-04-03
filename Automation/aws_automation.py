#!/usr/bin/python
#coding: utf-8

import boto3
import smtplib
import requests

# Credenciais para enviar e-mails
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "user@example.com"
smtp_password = "secret_password"
from_email = "alerts@example.com"
to_email = "recipient@example.com"

# Token de Bot do Telegram
telegram_token = "123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ"
telegram_chat_id = "1234567890"

# Inicialização da sessão boto3
s3 = boto3.resource('s3')

# Função para enviar alertas por e-mail
def send_email_alert(subject, body):
    message = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)

# Função para enviar alertas pelo Telegram
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&text={message}"
    requests.get(url)

# Monitoramento de buckets S3
for bucket in s3.buckets.all():
    current_objects = set()
    for obj in bucket.objects.all():
        current_objects.add(obj.key)

    # Verifica se houve mudanças nos objetos do bucket
    if current_objects != set(bucket.previous_objects):
        subject = f"Alerta: Mudanças no bucket S3 {bucket.name}"
        body = "Houve mudanças nos objetos deste bucket. Por favor, verifique."
        send_email_alert(subject, body)
        send_telegram_alert(subject + "\n" + body)

    # Atualiza a lista de objetos para o próximo monitoramento
    bucket.previous_objects = current_objects
