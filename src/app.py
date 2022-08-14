import uvicorn
from os import environ
from dotenv import load_dotenv

load_dotenv()
PORT = int(environ.get("PORT"))

if __name__ == "__main__":
    config = uvicorn.Config("services.server:app", port=PORT, host="0.0.0.0", log_level="info")
    server = uvicorn.Server(config)
    server.run()