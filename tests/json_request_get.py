import requests
import pandas as pd
import datetime as dt

headers_aai = {
    'authorization': "b350539a3b6f43d3b7d41125779ac686",
    'content-type': "application/json"
}

transcript_endpoint = "https://api.assemblyai.com/v2/transcript/"
id = "6dhlt92oie-a13e-4f5d-9c4c-727a503e8d4b"
polling_endpoint = transcript_endpoint + id

polling_response = requests.get(polling_endpoint, headers=headers_aai)
print(polling_response.json())
print('''
-----------------------------------------------------------------------------

'''
)
status = polling_response.json()["status"]
print(status)
print('''
-----------------------------------------------------------------------------

'''
)

if status == "completed":
    # Get the JSON file
    json_file = polling_response.json()
elif status == "error":
    raise Exception("Transcription failed.")

print('Transcript Done')
chapters = json_file['chapters']
for chapter in chapters:
    print(f"Summary: {chapter['summary']}")  
    print(f"Start: {chapter['start']}, End: {chapter['end']}")  
    print(f"Headline: {chapter['headline']}")  
    print(f"Gist: {chapter['gist']}")  
print('''
-----------------------------------------------------------------------------
'''
)

# Define a fuction to convert milliseconds to hhmmss
def millis_to_hhmmss(start_ms):
    hhmmss = dt.timedelta(milliseconds=start_ms)
    return str(hhmmss).split(".")[0]

chapters = polling_response.json()['chapters']
print(chapters)
print('''
-----------------------------------------------------------------------------
'''
)
chapters_df = pd.DataFrame(chapters)
print(chapters_df)
print('''
-----------------------------------------------------------------------------
'''
)
# # Replace <YOUR_FILE_NAME> with the name of your file
# file_name = "chapters_df1.txt"

# # Write the DataFrame to a text file
# with open(file_name, "w") as f:
#     f.write(chapters_df.to_string(index=False))
# chapters_df['start_str'] = chapters_df['start'].apply(millis_to_hhmmss)
# chapters_df['end_str'] = chapters_df['end'].apply(millis_to_hhmmss)

# for index, row in chapters_df.iterrows():
#     print(row['gist'])
#     print(row['summary'])
#     print(row['start_str'])
#     print(row['start'],)