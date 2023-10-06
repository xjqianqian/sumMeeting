import requests
from lib.config import auth_token

headers_aai = {
    'authorization': auth_token,
    'content-type': "application/json"
}
    
def upload_to_aai(audio_file):
    # Define the endpoint url
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = "https://api.assemblyai.com/v2/upload"
    # Upload the file to the upload endpoint
    print('uploading')
    upload_response = requests.post(
        upload_endpoint,
        headers=headers_aai, data=audio_file
    )
    # Get the audio_url from the json file
    audio_url = upload_response.json()['upload_url']
    print('Done')
    # Define what content you need for the transribing reponse 
    json_trans = {
        'audio_url': audio_url,
        'iab_categories': True,
        'auto_chapters': True
    }
    # Send audio for transcribing
    trans_response = requests.post(transcript_endpoint, json=json_trans, headers=headers_aai)
    print(trans_response.json())
    # Create a polling endpoint for checking transcribing status
    polling_endpoint = transcript_endpoint + "/" + trans_response.json()['id']
    return polling_endpoint

def convertMillis(start_ms):
    # Calculate the total seconds
    total_seconds = start_ms // 1000

    # Calculate the hours, minutes, and remaining seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    if hours < 0:
        # If hours are negative, display only minutes and seconds
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
    else:
        # Otherwise, format the result as "HH:MM:SS"
        time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return time_format
