from scripts.constants.app_configuration import Conf
import uvicorn
from fastapi import FastAPI
from scripts.core.services.service import app_router



app = FastAPI()
app.include_router(app_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host=Conf.SERVER_HOST, port=int(Conf.SERVER_PORT))
