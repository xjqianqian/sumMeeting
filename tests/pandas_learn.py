import pandas as pd
import datetime as dt

# Define a fuction to convert milliseconds to hhmmss
def millis_to_hhmmss(start_ms):
    hhmmss = dt.timedelta(milliseconds=start_ms)
    return str(hhmmss).split(".")[0]

transcrip_json = {
    'auto_chapters':'true',
    'chapters': [{'summary': 'Socrates helps you question life series. \
                  This program aims to make you feel unsure and perplexed through \
                  the use of extensive interrogative sentences. Today we will discuss \
                  university, a topic that the guest panel of AI talk is completely unfamiliar \
                  with.', 'gist': 'Socrates', 'headline': 'Socrates helps you question life series \
                    using extensive interrogative sentences', 'start': 650, 'end': 25830}, 
                {'summary': "Steve Jobs may have left college, but they didn't leave education. \
                 College is not unimportant, but there are certain things that cannot be taught. \
                 Education is a journey to develop an understanding of the world and its \
                 complexities. An unexamined life is not worth living.", 'gist': 'Socrates on \
                    College Life', 'headline': 'Socrates: Steve Jobs and Bill Gates left college \
                    to pursue unconventional wisdom', 'start': 25980, 'end': 334980}]
}

chapters = transcrip_json['chapters']
print(chapters)

chapters_df =pd.DataFrame(chapters)
print(chapters_df)

chapters_df['start_str'] = chapters_df['start'].apply(millis_to_hhmmss)
print(chapters_df['start_str'])
chapters_df['end_str'] = chapters_df['end'].apply(millis_to_hhmmss)
print(chapters_df['end_str'])
            
for index, row in chapters_df.iterrows():
    gist = row['gist']
    print(gist)
    summary = row['summary']
    print(summary)
    start_str = row['start_str']
    print(start_str)