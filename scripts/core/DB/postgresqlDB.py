from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select, update, delete
from scripts.logging.logger import logger

class sql_db:
    def __init__(self, url):
        self.url = url

    def create_table(self):
        engine = create_engine(self.url, echo=True)
        meta = MetaData()

        salva_table = Table(
            "salva", meta,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('course', String),
        )
        return engine, salva_table

    def creating(self, engine):
        meta = MetaData()
        meta.create_all(engine)


class sql_crud():
    def adding_rows(self, engine, salva_table, data):
        try:
            insert_statement = salva_table.insert().values(name=data.name, course=data.course)
            with engine.begin() as connection:
                connection.execute(insert_statement)
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")


    def returning_id(self, engine, salva_table, data):
        try:
            id_given = select(salva_table.c.id).where(salva_table.c.name == data.name)
            with engine.connect() as connection:
                result = connection.execute(id_given)
                row = result.fetchone()
            return row[0]
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def to_get_all_rows(self, engine, salva_table):
        try:
            with engine.connect() as connection:
                select_statement = select(salva_table)  # selecting
                result = connection.execute(select_statement)  # executing
                rows = result.fetchall()  # fetching
            return rows
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def id_checking(self, engine, salva_table, data):
        try:
            id_check = select(salva_table.c.id).where(salva_table.c.id == data.id)
            with engine.connect() as connection:
                result = connection.execute(id_check)
                row = result.fetchone()
            return row
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def updating(self, engine, salva_table, data):
        try:
            update_statement = (
                update(salva_table)
                .where(salva_table.c.id == data.id)
                .values(name=data.up_name, course=data.up_course)
            )
            with engine.begin() as connection:
                connection.execute(update_statement)
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def returning_specific_row(self, engine, salva_table, data):
        try:
            select_statement = select(salva_table).where(salva_table.c.id == data.id)
            with engine.connect() as connection:
                result = connection.execute(select_statement)
                row = result.fetchone()
            return row
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def to_delete_specific_row(self, engine, salva_table, data):
        try:
            delete_statement = delete(salva_table).where(salva_table.c.id == data.id)

            with engine.begin() as connection:
                connection.execute(delete_statement)
        except Exception as e:
            if connection is not None and connection.closed == False:
                connection.close()
            print("ERRORR-Connection is closed")
            print(str(e))
            logger.info("error-connection closed")

    def to_delete_table(self, engine, salva_table):
        salva_table.drop(engine)
