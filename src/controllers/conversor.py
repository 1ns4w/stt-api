import speech_recognition as sr

from database.database import Audio
from utils.convert_to_wav import convert_to_wav

class Conversor:

    @classmethod
    def convert_audio(cls, audio_file):
        sound = convert_to_wav(audio_file)
        print(len(sound.raw_data)/16000)

        r = sr.Recognizer()
        print('init')

        file_data = sr.AudioData(frame_data=sound.raw_data, sample_rate=8000, sample_width=2)

        return r.recognize_google(file_data, language = "es-PE")

    @classmethod
    async def insert_audio(cls, audio_file):
        audio_text = cls.convert_audio(audio_file)
        audio = Audio(audio_file_name = audio_file.filename, audio_text = audio_text)
        await audio.insert()
        print("Termino de insertar")