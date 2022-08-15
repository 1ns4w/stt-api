from controllers.conversor import Conversor
from fastapi import UploadFile, File, BackgroundTasks, APIRouter

router = APIRouter()

@router.post("/upload")
def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    
    background_tasks.add_task(Conversor.insert_audio, file)
    return {"success": "upload in progress", "file_name": file.filename}

"""
def start() :
    server = FastAPI()

    @server.post("/upload")
    async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
        try:
            background_tasks.add_task(Conversor.insert_audio, file)
            return {"success": "upload in progress", "file_name": file.filename}

        except Exception as e:
            return {"error": e.message, "file_name": file.filename}
"""