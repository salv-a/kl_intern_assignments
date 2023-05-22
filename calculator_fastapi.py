# from fastapi import FastAPI
#
# app = FastAPI()
# names = ['Imran', 'Salva', 'Sandeep']
#
# @app.get("/names")
# def root():
#     return {"names": names}

# @app.post('/add')
# def add_name(name):
#     names.append(name)
#     return {'names':names}

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "heyy i'm salva"}

from fastapi import FastAPI
from fastapi import Query


app = FastAPI()


@app.get("/add")
async def add(a: int = Query(..., description="The first number"),
              b: int = Query(..., description="The second number")):
    return {"result": a + b}


@app.get("/substract")
async def sub(a: int = Query(..., description="The first number"),
              b: int = Query(..., description="The second number")):
    return {"result": a - b}


@app.get("/multiply")
async def mult(a: int = Query(..., description="The first number"),
              b: int = Query(..., description="The second number")):
    return {"result": a * b}


@app.get("/divide")
async def div(a: int = Query(..., description="The first number"),
              b: int = Query(..., description="The second number")):
    return {"result": a / b}
