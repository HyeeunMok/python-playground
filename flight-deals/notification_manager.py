from twilio.rest import Client
import config

# Twilio
ACCOUNT_SID = config.twilio_account_sid
AUTH_TOKEN = config.twilio_auth_token
TWILIO_VIRTUAL_NUMBER = config.twilio_virtual_num
TWILIO_VERIFIED_NUMBER = config.twilio_verified_num


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.status)
