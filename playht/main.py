


import time
from pyht import Client
from pyht.client import TTSOptions
import os


userid = os.getenv("PLAY_HT_USER_ID")
api_key = os.getenv("PLAY_HT_API_KEY")

if userid is None or api_key is None:
    print('Please set the environment variables PLAY_HT_USER_ID and PLAY_HT_API_KEY')
    exit(1)

client = Client(
    user_id=userid,
    api_key=api_key,
)

options = TTSOptions(voice="s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",speed=5.0)
first = True
now = time.time()
for chunk in client.tts("Today is Sunday, the weather is sunny. I am here to test the delay of various TTS services thoroughly.", options):
    # do something with the audio chunk
    if first:
        first = False
        print('Pyht TTS Delay, Time to first chunk: ', time.time() - now)
        break