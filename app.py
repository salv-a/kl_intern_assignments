import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from scripts.core.services.sevice import college_router
from scripts.constant.app_configuration import Conf

app = FastAPI()
app.include_router(college_router)

if __name__ == '__main__':
    load_dotenv()
    uvicorn.run("main:app", host=Conf.SERVER_HOST, port=int(Conf.SERVER_PORT))
