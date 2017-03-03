import smtplib
from user_config import EMAIL_INFO

def send_email(message):
    """
    This function's input is a string with '\r\n' line endings.
    This function creates an email using Gmail's smtp server and the user's EMAIL_INFO and
    sends the email.
    """
    fromaddr = EMAIL_INFO['address']
    toaddrs = EMAIL_INFO['address']
    msg = "\r\n".join([
        "From: " + fromaddr,
        "To: " + toaddrs,
        "Subject: Trello Tasks for Today",
        "",
        message
    ])
    username = EMAIL_INFO['address']
    password = EMAIL_INFO['password']
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        return True
    except Exception as inst:
        print(inst)
        server.quit()
        return False
