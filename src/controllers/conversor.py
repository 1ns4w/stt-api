import speech_recognition as sr

from database.database import Audio
from utils.convert_to_wav import convert_to_wav

class Conversor:

    @classmethod
    def convert_audio(cls, audio_file):

        sound = convert_to_wav(audio_file)
        sound.export('audio.wav', format = "wav")

        r = sr.Recognizer()
        file_audio = sr.AudioFile('audio.wav')

        with file_audio as source:
            audio_text = r.record(source)

        return r.recognize_google(audio_text, language = "es-PE") 

    @classmethod
    async def insert_audio(cls, audio_file):
        audio_text = cls.convert_audio(audio_file)
        audio = Audio(audio_file_name = audio_file.filename, audio_text = audio_text)
        await audio.insert()
        print("Termino de insertar")