import streamlit as st
import requests
import pandas as pd
from lib.get_result import *
import datetime as dt

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
    # Transcribe the uploaded auido and initate the status
    polling_endpoint = upload_to_aai(upload_audio)
    status = 'submited'

    # Polling the status from the endpooint
    while status != 'completed':
        polling_response = requests.get(polling_endpoint, headers = headers_aai)
        print(polling_response.json())
        status = polling_response.json()['status']

        if status == 'completed':
            # Display categories
            st.subheader('Main themes of the meeting')
            with st.expander('Themes'):
                categories = polling_response.json()['iab_categories_result']['summary']
                for cat in categories:
                    st.markdown("* " + cat)
            # Display chapeter summaries
            st.subheader('Summary notes of the meeting')
            chapters = polling_response.json()['chapters']
            chapters_df = pd.DataFrame(chapters)
            chapters_df['start_str'] = chapters_df['start'].apply(millis_to_hhmmss)
            chapters_df['end_str'] = chapters_df['end'].apply(millis_to_hhmmss)
            
            for index, row in chapters_df.iterrows():
                with st.expander(row['gist']):
                    st.write(row['summary'])
                    st.button(row['start_str'], on_click=update_start, args=(row['start'],))
                    st.write(st.session_state) # Optional check session state