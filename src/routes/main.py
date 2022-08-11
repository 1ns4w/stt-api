import asyncio
import speech_recognition as sr

from database.database import Audio
from utils.convert_to_wav import convert_to_wav
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        sound = convert_to_wav(file)
        sound.export('audio.wav', format="wav")

        r = sr.Recognizer()
        file_audio = sr.AudioFile('audio.wav')

        with file_audio as source:
            audio_text = r.record(source)
            
        audio = Audio(audio_file_name=file.filename, audio_text=r.recognize_google(audio_text))
        asyncio.ensure_future(audio.insert())

        return {"success": "upload in progress", "file_name": file.filename}

    except Exception as e:
        return {"error": e.message, "file_name": file.filename}