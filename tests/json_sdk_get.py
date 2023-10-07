import assemblyai as aai
import datetime as dt
import pandas as pd

# Set API KEY
aai.settings.api_key = "b350539a3b6f43d3b7d41125779ac686"
# Get transcript by id
transcript = aai.Transcript.get_by_id("6dhlt92oie-a13e-4f5d-9c4c-727a503e8d4")




# print(transcript.id)
# print('''
# -----------------------------------------------------------------------------
# '''
# )
# print(transcript.text)
# print('''
# -----------------------------------------------------------------------------
# '''
# )
# print(transcript.status)
# print('''
# -----------------------------------------------------------------------------
# '''
# )

# print('Transcript Done')
# print('''
# -----------------------------------------------------------------------------
# '''
# )
# # Get iab categories result
# categories = transcript.iab_categories.summary
# for category in categories:
#     print("* " + category)
# print('''
# -----------------------------------------------------------------------------
# '''
# )




# Define a fuction to convert milliseconds to hhmmss
def millis_to_hhmmss(start_ms):
    hhmmss = dt.timedelta(milliseconds=start_ms)
    return str(hhmmss).split(".")[0]

# Get chapters
chapters = transcript.chapters
print(chapters)
print('''
-----------------------------------------------------------------------------
'''
)
# # Print chapters
# for chapter in chapters:
#     print(f"Summary: {chapter.gist}")  
#     print(f"Start: {chapter.start}, End: {chapter.end}")  
#     print(f"Headline: {chapter.headline}")  
#     print(f"Gist: {chapter.summary}")  
chapters_df = pd.DataFrame([vars(chapter) for chapter in chapters])
# chapters_df = pd.DataFrame(chapters, columns=['summary', 'headline', 'gist', 'start', 'end'])
print(chapters_df)
print(chapters_df['start'])

# # Replace <YOUR_FILE_NAME> with the name of your file
# file_name = "chapters_df.txt"

# # Write the DataFrame to a text file
# with open(file_name, "w") as f:
#     f.write(chapters_df.to_string(index=False))

print('''
-----------------------------------------------------------------------------
'''
)
print(chapters_df['gist'])
chapters_df['start_str'] = chapters_df['start'].apply(millis_to_hhmmss)
chapters_df['end_str'] = chapters_df['end'].apply(millis_to_hhmmss)

for index, row in chapters_df.iterrows():
    print(row['gist'])
    print('''
-----------------------------------------------------------------------------
'''
)
    print(row['summary'])
    print('''
-----------------------------------------------------------------------------
'''
)
    print(row['start_str'])