from pydub import AudioSegment
from fastapi import UploadFile, File

def convert_to_wav(file):
    contents = file.file.read()

    with open(file.filename, 'wb') as f:
        f.write(contents)

    try:
        sound = AudioSegment.from_mp3(file.filename)
        print("Convirtiendo de mp3 a wav")
    except:
        sound = AudioSegment.from_file(file.filename, format="mp4")
        print("Convirtiendo de mp4 a wav")

    return sound