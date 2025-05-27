from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\edw50\Downloads\ffmpeg-2025-05-26-git-43a69886b2-full_build\bin"

app = FastAPI()

# Load whisper model
model = whisper.load_model("tiny")

# CORS configuration (kept for if you want to use API later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def local_transcribe(file_path: str):
    """Directly transcribe a local file"""
    result = model.transcribe(file_path)
    return {
        "text": result["text"],
        "language": result["language"]
    }

