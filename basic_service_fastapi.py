from fastapi import FastAPI

app = FastAPI()  # creating instance of fastapi


@app.get("/ab")  # route
async def message():
    return {"Salva": "Intern"}

@app.get("/about")
async def message2():
    return {"message":"heyy im salva"}