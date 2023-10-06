import assemblyai as aai
import os

# Set API KEY
aai.settings.api_key = os.getenv("AAI_API_KEY")
# Set transcription config
config=aai.TranscriptionConfig(auto_chapters=True)
# Transcribing
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

for chapter in transcript.chapters:
    print(f"Summary: {chapter.summary}")  
    print(f"Start: {chapter.start}, End: {chapter.end}")  
    print(f"Headline: {chapter.headline}")  
    print(f"Gist: {chapter.gist}")  