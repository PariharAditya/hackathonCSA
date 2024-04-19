import os
from dotenv import load_dotenv
from google.cloud import speech
load_dotenv()
os.environ['GOOGLE_APPLICATION_CREDENTIALS']
def transcribe_audio(audio_file_path):

    client = speech.SpeechClient()

    # Loads the audio file into memory
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US"
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

# Example use
transcribe_audio("latest_recording.wav")
