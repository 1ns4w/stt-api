import mongox

client = mongox.Client("mongodb://localhost:27017")
db = client.get_database("stt")

class Audio(mongox.Model):
    audio_file_name: str
    audio_text: str

    class Meta:
        collection = db.get_collection("audios")