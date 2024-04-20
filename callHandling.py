from dotenv import load_dotenv
from twilio.rest import Client
import requests
import os
import time
from twilio.twiml.voice_response import VoiceResponse


load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Twilio Account Credentials
ACCOUNT_SID = 'AC47ceb83852bf91bd3e45102b6c000e5f'
AUTH_TOKEN = '04ec7ce094f163dd1bdaf8ee20e7f477'
TWILIO_PHONE_NUMBER = '+18603658310'
TO_PHONE_NUMBER = '+917488156949'

client = Client(account_sid, auth_token)

def handle_call():
    response = VoiceResponse()
    response.say("Hello, thank you for calling. Please state your problem after the tone.")
    response.record(timeout=10, transcribe=True)

    # Create a new outgoing call and use the 'respond_to_call' TwiML for the call
    call = client.calls.create(
        twiml=str(response),
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER
    )

def download_and_transcribe():
    recordings = client.recordings.list(limit=1)
    for recording in recordings:
        recording_uri = "https://api.twilio.com" + recording.uri.replace('.json', '.wav')
        response = requests.get(recording_uri, stream=True, auth=(account_sid, auth_token))
        with open(f'recording.wav', 'wb') as out_file:
            out_file.write(response.content)
        print('Downloaded recording.wav')

        while True:
            transcriptions = client.transcriptions.list()
            for transcription in transcriptions:
                if transcription.recording_sid == recording.sid:
                    print(transcription.transcription_text)
                    return
            print('Waiting for transcription...')
            time.sleep(10)

handle_call()
download_and_transcribe()