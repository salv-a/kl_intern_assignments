from scripts.logging.logger import logger
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select, update, delete
from scripts.constants.app_constant import Sql
from scripts.core.DB.postgresqlDB import sql_db


class Table_creator():
    def creating(self):
        sql_db_obj = sql_db(Sql.sql_url)
        engine, salva_table = sql_db_obj.create_table()

        table_check = inspect(engine)
        table_exists = table_check.has_table("salva")

        if table_exists:
            print(
                "------------------------------------Table exists in the database.--------------------------------")
            logger.info("Table exists in the database.")
        else:
            print("--------------------------Table does not exist in the database.-------------------------------")
            logger.info("Table does not exist in the database")
            sql_db_obj.creating(engine)
            print("---------------------------Table is created---------------------------------------")
            logger.info("Table is created")
        return engine, salva_table
