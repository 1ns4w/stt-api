import mongox
from os import environ
from dotenv import load_dotenv

load_dotenv()
client = mongox.Client(environ.get("MONGODB_URI") or "mongodb://localhost:27017")
db = client.get_database("stt")

class Audio(mongox.Model):
    audio_file_name: str
    audio_text: str

    class Meta:
        collection = db.get_collection("audios")