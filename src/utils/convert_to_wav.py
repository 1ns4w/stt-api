from pydub import AudioSegment
from io import BytesIO

def convert_to_wav(file) -> AudioSegment:
    rawFile = file.file.read()
    s = BytesIO(rawFile)
    sound = AudioSegment.from_file(s)
    return sound