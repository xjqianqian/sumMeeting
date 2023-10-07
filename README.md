# Introduction
Upload a meeting auido file (eg. *.mp3) , transcribe the audio use AssemblyAI. Addtionally, use AssemblyAI's advance feature **auto chapter, iab_categories** to get summary and relavant topics.

# Run locally in windows
## Install dependencies
```CMD
pip install -r requirement
```

## Run streamlit
```CMD
streamlit run summeeting.py
```

# To Be Done
1. Update the old code with endpoint to the latest AAI SDK 'transcriber'.
2. Add progress bar to see the transcribing progress