# lyti aatf vjqm zjab
import smtplib
import os 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(".env")

#* Definir las credenciales
remitente = "torresdrichar@gmail.com"
password = os.getenv("KEY_EMAIL")

#* Definir los detalles del destinatario 
destinatario = "motinaruto@gmail.com"
asunto = "Prueba de correo"

#* Crear mensaje

mensaje =  MIMEMultipart()
mensaje["From"] = remitente
mensaje["To"] =destinatario
mensaje["Subject"] = asunto

#* Agregar el cuerpo del mensaje
cuerpo = "Este es el cuerpo del email"
mensaje.attach(MIMEText(cuerpo,"plain"))

#* Iniciar sesion en servidor SMTP de gmail
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(remitente, password)

#* Enviar correo

texto = mensaje.as_string()
server.sendmail(remitente,destinatario,texto)
server.quit()

print("Correo enviado")