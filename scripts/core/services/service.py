from fastapi import APIRouter
from schemas.models import to_register
from scripts.logging.logger import logger
from schemas.models import to_update
from schemas.models import to_delete
from scripts.constants.app_constant import APis
from scripts.core.handlers.table_crud_handler import Table_handler
from scripts.core.handlers.table_handler import Table_creator

app_router = APIRouter()

# creating table
try:
    table_creator_obj = Table_creator()
    engine, salva_table = table_creator_obj.creating()
except Exception as e:
    print("--------------------ERROORR--------------------")
    print(str(e))
    logger.warning("Something is wrong with creating table")


@app_router.get(APis.intro)
def intro():
    return {"WELCOME TO SQL DATABASE"}


@app_router.post(APis.to_add_data)
def registering(data: to_register):
    try:
        return Table_handler().to_register(engine, salva_table, data)
    except Exception as e:
        print("--------------------ERROORR--------------------")
        print(str(e))
        logger.warning("Something is wrong with adding rows")
        return "ERRORR"


@app_router.get(APis.to_view_data)
def display_table():
    try:
        table_object = Table_handler()
        return table_object.to_view(engine, salva_table)
    except Exception as e:
        print("--------------------------------ERRORR-----------------------------")
        print(str(e))
        logger.warning("error")
        return "ERRORR"


@app_router.put(APis.to_update)
def updating(data: to_update):
    try:
        return Table_handler().to_change(engine, salva_table, data)
    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        logger.warning("error")
        return "ERRORRRR"


@app_router.delete(APis.to_delete)
def deleting(data: to_delete):
    try:
        return Table_handler().to_erase(engine, salva_table, data)
    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        logger.warning("errorr")
        return "ERRORRRR"


@app_router.delete(APis.to_delete_table)
def del_table():
    try:
        return Table_handler().delete_table(engine, salva_table)
    except Exception as e:
        print("-----------------------------ERRORR-----------------")
        print(str(e))
        logger.warning("errorr")
        return "ERRORRRR"
