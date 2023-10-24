


import os
import time
import requests


voice_id = '21m00Tcm4TlvDq8ikWAM'


CHUNK_SIZE = 512
url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id  +"/stream"

xi_api_key = os.getenv('ELEVENLAB_KEY')


if xi_api_key is None:
    print('Please set the environment variable ELEVENLAB_KEY')
    exit(1)

text = "Today is Sunday, the weather is sunny. I am here to test the delay of various TTS services thoroughly"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": xi_api_key
}

data = {
  "text": text,
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

now = time.time()
response = requests.post(url, json=data, headers=headers, stream=True)


first = True
for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
    if first:
        first = False
        print('Elevenlab TTS Delay, Time to first chunk: ', time.time() - now)
        break
