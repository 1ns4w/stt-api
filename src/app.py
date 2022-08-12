import uvicorn
from routes.main import start

async def app(scope, receive, send):
    start()

if __name__ == "__main__":
    config = uvicorn.Config("app:app", port=5050, log_level="info")
    server = uvicorn.Server(config)
    server.run()