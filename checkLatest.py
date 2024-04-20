import requests
from twilio.rest import Client

# Twilio Account Credentials
ACCOUNT_SID = 'AC47ceb83852bf91bd3e45102b6c000e5f'
AUTH_TOKEN = '04ec7ce094f163dd1bdaf8ee20e7f477'
TWILIO_PHONE_NUMBER = '+18603658310'
TO_PHONE_NUMBER = '+917488156949'

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# List recordings and retrieve the latest one
latest_recording = None
latest_date = None
for recording in client.recordings.list():
    recording_date = recording.date_created
    if latest_date is None or recording_date > latest_date:
        latest_recording = recording
        latest_date = recording_date

# Download the latest recording
if latest_recording:
    recording_uri = "https://api.twilio.com" + latest_recording.uri.replace('.json', '.wav')
    response = requests.get(recording_uri, stream=True, auth=(ACCOUNT_SID, AUTH_TOKEN))
    with open('latest_recording.wav', 'wb') as out_file:
        out_file.write(response.content)
    print('Latest recording downloaded successfully.')
else:
    print('No recordings found.')