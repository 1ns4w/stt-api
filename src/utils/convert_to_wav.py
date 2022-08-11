from pydub import AudioSegment
from fastapi import UploadFile, File

def convert_to_wav(file: UploadFile = File(...)):
    contents = file.file.read()

    with open(file.filename, 'wb') as f:
        f.write(contents)

    try:
        sound = AudioSegment.from_mp3(file.filename)
    except:
        sound = AudioSegment.from_file(file.filename, format="mp4")

    return sound