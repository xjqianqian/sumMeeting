import streamlit as st
import pandas as pd
import datetime as dt
import assemblyai as aai
from lib.config import auth_token
import io, os

# Define a function to upload audio to AAI using assemblyai SDK
def aai_transcribe_sdk(audio_file):
    # Set API KEY from environment or from config.py, chosee 1 of the 2
    # aai.settings.api_key = os.getenv("AAI_API_KEY")
    aai.settings.api_key = auth_token
    # Set transcription config
    config=aai.TranscriptionConfig(auto_chapters=True, iab_categories=True)
    # Transcribing
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_file)
    return transcript

# Create a file uploader for audio file
upload_audio = st.file_uploader('Please upload a audio file:')

# Initialize the start point when audio is played to zero 
if 'start_point' not in st.session_state:
    st.session_state['start_point'] = 0
# Define a fuction to update the start point by a given time
def update_start(start_t):
    st.session_state['start_point'] = int(start_t/1000)
# Define a fuction to convert milliseconds to hhmmss
def millis_to_hhmmss(start_ms):
    hhmmss = dt.timedelta(milliseconds=start_ms)
    return str(hhmmss).split(".")[0]

# If audio is uploaded, display it and start to transcribe
if upload_audio is not None:
    # Display the audio in the page
    st.audio(upload_audio,start_time=st.session_state['start_point'])
    # Transcribe the uploaded auido and initialize the status
    transcript = aai_transcribe_sdk(audio_file=io.BytesIO(upload_audio.read()))
    status = 'submited'

    # Polling the status from the endpooint
    while status != 'completed':
        status = str(transcript.status).split(".")[1]
        if status == 'completed':
            # Display categories
            st.subheader('Main themes of the meeting')
            with st.expander('Themes'):
                categories = transcript.iab_categories.summary
                for cat in categories:
                    st.markdown("* " + cat)
            # Display chapeter summaries
            st.subheader('Summary notes of the meeting')
            chapters = transcript.chapters
            chapters_df = pd.DataFrame([vars(chapter) for chapter in chapters])
            chapters_df['start_str'] = chapters_df['start'].apply(millis_to_hhmmss)
            chapters_df['end_str'] = chapters_df['end'].apply(millis_to_hhmmss)
            
            for index, row in chapters_df.iterrows():
                with st.expander(row['gist']):
                    st.write(row['summary'])
                    st.button(row['start_str'], on_click=update_start, args=(row['start'],))
                    st.write(st.session_state) # Optional check session state