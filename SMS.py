import os
from twilio.rest import Client
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_sms(text: str):
    message = client.messages \
        .create(
            body=text,
            from_='+12568294379',
            to='+380503962864'
        )


