from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import speech_recognition as sr

from database.database import Audio
from utils.convert_to_wav import convert_to_wav

app = FastAPI()

@app.post("/upload")
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    async def insertData(audio_text2):
        audio = Audio(audio_file_name="Pollito con papas", audio_text=audio_text2)
        await audio.insert()
        print("Termino de insertar")
    try:
        sound = convert_to_wav(file)
        sound.export('audio.wav', format="wav")

        r = sr.Recognizer()
        file_audio = sr.AudioFile('audio.wav')

        with file_audio as source:
            audio_text = r.record(source)

        audio_text2 = r.recognize_google(audio_text) 
        
        background_tasks.add_task(insertData, audio_text2)

        return {"success": "upload in progress", "file_name": file.filename}

    except Exception as e:
        return {"error": e.message, "file_name": file.filename}