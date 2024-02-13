import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

smtp_gmail_address = "smtp.gmail.com"
port = 465

sender = "carlostranquilino.cr@gmail.com"
subject = "Good Morning!"
body = """
        Good day sunshine 
        Good day sunshine 
        Good day sunshine
        I need to laugh, and when the sun is out
        I've got something I can laugh about
        I feel good, in a special way
        I'm in love and it's a sunny day
        """

password = os.getenv('APP_PASSWORD')
recipient = [sender,"xdeus_v2@outlook.com"]


def send_email(subject,body,sender,recipient,password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)

    with smtplib.SMTP_SSL(smtp_gmail_address,465) as smtp_server:
        smtp_server.login(sender,password)
        smtp_server.sendmail(sender,recipient,msg.as_string())
    print("Message sent!")

send_email(subject,body,sender,recipient,password)
