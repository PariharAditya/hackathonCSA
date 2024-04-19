import os
import time
from google.cloud import speech
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

ACCOUNT_SID = 'AC47ceb83852bf91bd3e45102b6c000e5f'
AUTH_TOKEN = '04ec7ce094f163dd1bdaf8ee20e7f477'
TWILIO_PHONE_NUMBER = '+18603658310'
TO_PHONE_NUMBER = '+917488156949'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def respond_to_call():
    response = VoiceResponse()
    response.say("Hello, thank you for calling. Please state your problem after the tone.")
    response.record(timeout=100, transcribe=True)
    return str(response)

# Create a new outgoing call and use the 'respond_to_call' TwiML for the call
call = client.calls.create(
    twiml=respond_to_call(),
    to=TO_PHONE_NUMBER,
    from_=TWILIO_PHONE_NUMBER
)

print(f"Started call {call.sid}")

# List all recordings
recordings = client.recordings.list()
for recording in recordings:
    print(recording.uri)

# Call recordings.py
time.sleep(30)
os.system('python recordings.py')
