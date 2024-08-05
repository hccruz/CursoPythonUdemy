# Enviando emails com Python

import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

# Dados do remetente e destinatário
SENDER = os.getenv('SENDER', '')
PASSWORD = os.getenv('PASSWORD', '')
RECEIVER = os.getenv('RECEIVER', '')

# Configurações do SMTP
HOST = 'smtp.gmail.com'
PORT = 587
USER = SENDER
PASSWORD = PASSWORD

# Mensagem de text
SUBJECT = 'Assunto'
