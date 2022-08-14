import mongox
from os import environ
from dotenv import load_dotenv

load_dotenv()

client = mongox.Client(environ.get("MONGODB_URI"))
db = client.get_database(environ.get("DATABASE_NAME"))

class Audio(mongox.Model):
    audio_file_name: str
    audio_text: str

    class Meta:
        collection = db.get_collection("audios")