import uvicorn
from os import environ
from dotenv import load_dotenv

load_dotenv()
PORT = environ.get("PORT")

if __name__ == "__main__":
    config = uvicorn.Config("services.server:app", port=PORT, log_level="info")
    server = uvicorn.Server(config)
    server.run()