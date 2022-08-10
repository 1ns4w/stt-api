from fastapi import FastAPI, File, UploadFile
from pydub import AudioSegment
import speech_recognition as sr
from os import path
from pydub.utils import which

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)

    except Exception:
        return {"error": "There was an error uploading the file"}

    try:
        sound = AudioSegment.from_mp3(file.filename)
    except:
        sound = AudioSegment.from_file(file.filename, format="mp4")

    sound.export('audio.wav', format="wav")

    r = sr.Recognizer()
    file_audio = sr.AudioFile('audio.wav')

    with file_audio as source:
        audio_text = r.record(source)

    return {"success": r.recognize_google(audio_text)}