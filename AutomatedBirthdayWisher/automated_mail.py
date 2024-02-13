import datetime as dt
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
import smtplib

# LOAD ENV VARIABLES
load_dotenv()

"""
VARIABLES OF THE BIRTHDAY PERSON THAT WILL RECEIVE THE AUTOMATED MESSAGE
"""
YEAR_OF_BIRTH = 1998
MONTH_OF_BIRTH = 2 
DAY_OF_BIRTH = 13 
HOUR_OF_CONGRATULATIONS = 10    # Hour of 
MINUTE_OF_CONGRATULATIONS = 45  # message 10:45
birthday_message_sent = False
"""
CREATE AN OBJECT WITH CURRENT DATE AND TIME 
"""
now = dt.datetime.now()
month = now.month
day = now.day
hour = now.hour
minute = now.minute

"""
PARAMETERS OF THE BIRTHDAY AUTOMATED MESSAGE
"""
smtp_gmail_address = "smtp.gmail.com"
port = 465

sender = "carlostranquilino.cr@gmail.com"
subject = "Happy Birthday!"
body = """
        “Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!”
        """

password = os.getenv('APP_PASSWORD')
recipient = [sender,"xdeus_v2@outlook.com"]

"""
SEND EMAIL FUNCTION 

"""


def send_email(subject,body,sender,recipient,password):
    global birthday_message_sent
    if (MONTH_OF_BIRTH == month and DAY_OF_BIRTH == day and HOUR_OF_CONGRATULATIONS == hour and MINUTE_OF_CONGRATULATIONS == minute and birthday_message_sent==False):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipient)

        with smtplib.SMTP_SSL(smtp_gmail_address,port) as smtp_server:
            smtp_server.login(sender,password)
            smtp_server.sendmail(sender,recipient,msg.as_string())
        birthday_message_sent=True
    else:
        birthday_message_sent=False


while birthday_message_sent == False:
    send_email(subject,body,sender,recipient,password)


  
