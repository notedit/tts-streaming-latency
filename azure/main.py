

import os
import time
import azure.cognitiveservices.speech as speechsdk


speech_key = os.getenv('SPEECH_KEY')
speech_regoion = os.getenv('SPEECH_REGION')

if speech_key is None or speech_regoion is None:
    print('Please set the environment variables SPEECH_KEY and SPEECH_REGION')
    exit(1)


text = 'Today is Sunday, the weather is sunny. I am here to test the delay of various TTS services thoroughly'

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_regoion)

speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'
speech_config.speech_synthesis_language = "en-US"

speech_config.set_speech_synthesis_output_format(
    speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)

# Creates an audio output stream
pull_stream = speechsdk.audio.PullAudioOutputStream()
# Creates a speech synthesizer using pull stream as audio output.
stream_config = speechsdk.audio.AudioOutputConfig(stream=pull_stream)
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=stream_config)



speech_synthesizer.speak_text_async(text)

start = time.perf_counter()

first = True
while True:
    audio_buffer = bytes(512)
    filled_size = pull_stream.read(audio_buffer)
    if first:
        first = False
        end = time.perf_counter()
        print('Azure TTS Delay, Time to first chunk: ', end - start)
        break

