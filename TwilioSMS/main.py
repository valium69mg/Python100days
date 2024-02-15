
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone = os.getenv('TWILIO_ACCOUNT_PHONE')
my_phone = "+524422737383"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Bacon.",
                     from_=twilio_phone,
                     to=my_phone
                 )

print(message.sid)