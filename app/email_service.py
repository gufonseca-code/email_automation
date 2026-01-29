import smtplib
from email.message import EmailMessage
from app.config import Config

def send_email(subject, body, recipients, attachments=None):
    msg = EmailMessage()
    msg["from"] = Config.EMAIL_ADDRESS
    msg['To'] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(body)

    if attachments:
        for filename, mimetype, data in attachments:
            maintype, subtype = mimetype.split("/", 1)
            msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=filename)
           


    with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
        server.starttls()
        server.login(Config.EMAIL_ADDRESS, Config.EMAIL_PASSWORD)
        server.send_message(msg)
