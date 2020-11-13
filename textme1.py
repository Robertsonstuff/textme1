
# Download the helper library from https://www.twilio.com/docs/python/install
import os

from twilio.rest import Client


twilio_num = os.environ['TWILIO_NUMBER']
personal_num = os.environ['MY_NUMBER']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
def send_goodtimes():
    message = client.messages \
                .create(
                     body="OMG! I am awesome!!!",
                     from_='twilio_num',
                     to='personal_num'
                 )
    print(message.sid)