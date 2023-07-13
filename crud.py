# # if __name__ == "__main__":
# #
# #     uvicorn.run("crud:app", host="0.0.0.0", port=8000, reload=True)

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select, update, delete
from pydantic import BaseModel
from fastapi import FastAPI

engine = create_engine('postgresql://interns:interns%40123@192.168.0.220:5432/internsb2', echo=True)
meta = MetaData()

app = FastAPI()


class table(BaseModel):
    name: str


class to_register(BaseModel):
    name: str
    course: str


class to_update(BaseModel):
    id: int
    up_name: str
    up_course: str


class to_delete(BaseModel):
    id: int


try:
    salva_table = Table(
        "salva", meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('course', String),
    )

    table_check = inspect(engine)
    table_exists = table_check.has_table("salva")

    if table_exists:
        print("------------------------------------Table exists in the database.--------------------------------")
    else:
        print("--------------------------Table does not exist in the database.-------------------------------")
        meta.create_all(engine)
        print("---------------------------Table is created---------------------------------------")
except Exception as e:
    print("------------------------------------ERRORR---------------------------------")
    print(str(e))

@app.get("/")
def intro():
    return "WELCOME TO SQL DATABASE"

@app.post("/student_registration")
def registering(data: to_register):
    try:
        insert_statement = salva_table.insert().values(name=data.name, course=data.course)
        with engine.begin() as connection:
            connection.execute(insert_statement)
        print("------------------------------successfully registered--------------------------------")
        id_given = select(salva_table.c.id).where(salva_table.c.name == data.name)
        with engine.connect() as connection:
            result = connection.execute(id_given)
            row = result.fetchone()
        return "successfully registered and your id=" + str(row[0])
    except Exception as e:
        print("--------------------ERROORR--------------------")
        print(str(e))
        return "ERRORR"


@app.get("/to_read_data")
def display_table():
    try:
        with engine.connect() as connection:
            select_statement = select(salva_table)  # selecting
            result = connection.execute(select_statement)  # executing
            rows = result.fetchall()  # fetching
            list = []
            for row in rows:
                id, name, lastname = row
                print(f"ID: {id}, Name: {name}, Lastname: {lastname}")
                list.append([(f"ID: {id}, Name: {name}, Lastname: {lastname}")])
            return list
    except Exception as e:
        print("--------------------------------ERRORR-----------------------------")
        print(str(e))
        return "ERRORR"


@app.post("/to_update")
def updating(data: to_update):
    try:
        id_check = select(salva_table.c.id).where(salva_table.c.id == data.id)
        with engine.connect() as connection:
            result = connection.execute(id_check)
            row = result.fetchone()
        if row != None:

            update_statement = (
                update(salva_table)
                .where(salva_table.c.id == data.id)
                .values(name=data.up_name, course=data.up_course)
            )
            with engine.begin() as connection:
                connection.execute(update_statement)

            select_statement = select(salva_table).where(salva_table.c.id == data.id)
            with engine.connect() as connection:
                result = connection.execute(select_statement)
                row = result.fetchone()
                print(row)
            return f"row is updated as {row}"
        else:
            return "This id is not present"
    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        return "ERRORRRR"


@app.delete("/to_delete")
def deleting(data: to_delete):
    try:
        id_check = select(salva_table.c.id).where(salva_table.c.id == data.id)
        with engine.connect() as connection:
            result = connection.execute(id_check)
            row = result.fetchone()
        if row != None:
            delete_statement = delete(salva_table).where(salva_table.c.id == data.id)

            with engine.begin() as connection:
                connection.execute(delete_statement)

            select_statement = salva_table.select().where(salva_table.c.id == data.id)
            with engine.connect() as connection:
                result = connection.execute(select_statement)
                row = result.fetchone()
                print(row)
            return "row is deleted successfully"
        else:
            return "This id is not present"

    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        return "ERRORRRR"


@app.post("/delete/table")
def del_table():
    try:
        salva_table.drop(engine)
        return "table deleted successfully"
    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        return "ERRORRRR"

# interns
# interns@123
# 192.168.0.220: 5432
# postgresql://interns:interns%40123@192.168.0.220:5432/internsb2
