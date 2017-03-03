import smtplib
from config import EMAIL_INFO

def send_email(message):
    fromaddr = EMAIL_INFO['address']
    toaddrs  = EMAIL_INFO['address']
    msg = "\r\n".join([
    "From: " + fromaddr,
    "To: " + toaddrs,
    "Subject: Trello Tasks for Today",
    "",
    message
    ])
    username = EMAIL_INFO['address']
    password = EMAIL_INFO['password']
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

