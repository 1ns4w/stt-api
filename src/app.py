import uvicorn



if __name__ == "__main__":
    config = uvicorn.Config("services.server:app", port=5050, log_level="info")
    server = uvicorn.Server(config)
    server.run()