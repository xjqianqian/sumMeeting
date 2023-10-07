import assemblyai as aai
from lib.config import auth_token
import os

'''
Set API KEY from environment or from config.py, chosee 1 of the 2
'''
# aai.settings.api_key = os.getenv("AAI_API_KEY")
aai.settings.api_key = auth_token

def aai_transcribe_sdk(audio_file):
  # Set transcription config
  config=aai.TranscriptionConfig(auto_chapters=True, iab_categories=True)
  # Transcribing
  transcriber = aai.Transcriber(config=config)
  transcript = transcriber.transcribe(audio_file)
  print('Transcript Done')
  for chapter in transcript.chapters:
      print(f"Summary: {chapter.summary}")  
      print(f"Start: {chapter.start}, End: {chapter.end}")  
      print(f"Headline: {chapter.headline}")  
      print(f"Gist: {chapter.gist}")  