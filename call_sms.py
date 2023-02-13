import os
from twilio.rest import Client


account_sid ="AC00b7a7dd2bca720a785402160e64281d"
auth_token = "7e7faee298a5a6f614aa138f85f52f24"
client = Client(account_sid, auth_token)
from_number="+12602611318"


class Call_Sms:

    def __init__(self,to_number) -> None:
        self.to_number=to_number

    
    def Call_alert(self,voice_text):
        client.calls.create(
                    twiml=f'<Respons><Say>{voice_text}</Say></Response>',
                    to=self.to_number,
                    from_=from_number
                   )
        
    def Sms_alert(self,sms_message):
        client.messages.create(
         body=sms_message,
         from_=from_number,
         to=self.to_number
     )





