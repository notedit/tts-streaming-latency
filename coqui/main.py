

import os
import sys
import requests
import time



voice_id = 'c791b5b5-0558-42b8-bb0b-602ac5efc0b9'

text = 'Today is Sunday, the weather is sunny. I am here to test the delay of various TTS services thoroughly'


COQUI_API_TOKEN = os.getenv("COQUI_TOKEN")

if COQUI_API_TOKEN is None:
    print('Please set the environment variable COQUI_TOKEN')
    exit(1)


start = time.perf_counter()
res = requests.post(
    "https://app.coqui.ai/api/v2/samples/xtts/stream",
    json={ 
        "text": text, 
        "language": 'en', 
        "voice_id": voice_id},
        headers={"Authorization": f"Bearer {COQUI_API_TOKEN}"},
        stream=True,
    )

if res.status_code != 201:
    print(f"Endpoint failed with status code {res.status_code}:",
            res.content.decode("utf-8"))
    sys.exit(1)

first = True
for chunk in res.iter_content(chunk_size=512):
    if first:
        end = time.perf_counter()
        print(f"Coqui TTS Delay, Time to first chunk: {end-start}s")
        first = False
        break

