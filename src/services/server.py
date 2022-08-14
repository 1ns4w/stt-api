from fastapi import FastAPI
from routes.main import router

app = FastAPI()

app.include_router(router, prefix='/api')

@app.get("/")
def index():
    return {"message": "Hello World"}