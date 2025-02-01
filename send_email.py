import smtplib,ssl
import os

host="smtp.gmail.com"
port=465

def send_email(message,sender="ykcspor@gmail.com"):
    username="ykcspor@gmail.com" #from
    password="tfmk kjft zhos oteu"
    password=os.getenv("PASSWORD")

    receiver="ykcspor@gmail.com" #to

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(sender,receiver,message)