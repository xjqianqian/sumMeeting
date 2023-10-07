# Introduction
During a meeting, transcribe the audio from the computer audio system to get realtime caption, summary, and action.
## Dependencies
[Recall.ai](https://www.recall.ai/) provides a single API for accessing real-time meeting data from platforms like Zoom, Microsoft Teams, Google Meet, and more. 

# Run locally in Windows
## Install Node.js and npm
Go to the [node website](https://nodejs.org/en/download/) and download the installer that is appropriate for your machine, likely the 64-bit Windows installer or the 64-bit macOS installer.

## Install Ngrok
Ngrok is a reverse proxy that lets you expose your local machine to the internet safely. 
```CMD
# MacOS
brew install ngrok/ngrok/ngrok

# Windows
choco install ngrok
```

## Get Recall.ai API key and setup in the env
go to the [recall.ai/AssemblyAI webpage](https://www.recall.ai/partners/assemblyai) and click "Get the integration". Currently, this service is available by invite only, but exclusive access is provided for AssemblyAI customers.