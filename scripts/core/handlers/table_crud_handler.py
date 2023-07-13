from scripts.logging.logger import logger
from scripts.core.DB.postgresqlDB import sql_crud


class Table_handler:
    def to_register(self, engine, salva_table, data):

        sql_crud_obj = sql_crud()
        sql_crud_obj.adding_rows(engine, salva_table, data)

        print("------------------------------successfully registered--------------------------------")
        logger.info("successfully registered")
        id = sql_crud_obj.returning_id(engine, salva_table, data)
        return "successfully registered and your id=" + str(id)

    def to_view(self, engine, salva_table):

        sql_crud_obj = sql_crud()
        rows = sql_crud_obj.to_get_all_rows(engine, salva_table)
        list = []
        for row in rows:
            id, name, lastname = row
            print(f"ID: {id}, Name: {name}, Lastname: {lastname}")
            list.append([f"ID: {id}, Name: {name}, Lastname: {lastname}"])
        logger.info("data is returned as list")
        return list

    def to_change(self, engine, salva_table, data):
        sql_crud_obj = sql_crud()
        row = sql_crud_obj.id_checking(engine, salva_table, data)
        if row != None:
            sql_crud_obj = sql_crud()
            sql_crud_obj.updating(engine, salva_table, data)
            logger.info("row is updated")
            sql_crud_obj = sql_crud()
            row = sql_crud_obj.returning_specific_row(engine, salva_table, data)
            print(row)
            return f"row is updated as {row}"
        else:
            logger.info("this id is not present,so updation is not succesful")
            return "This id is not present"

    def to_erase(self, engine, salva_table, data):
        sql_crud_obj = sql_crud()
        row = sql_crud_obj.id_checking(engine, salva_table, data)
        if row != None:
            sql_crud_obj = sql_crud()
            sql_crud_obj.to_delete_specific_row(engine, salva_table, data)
            logger.info("row deleted successfully")

            select_statement = salva_table.select().where(salva_table.c.id == data.id)
            with engine.connect() as connection:
                result = connection.execute(select_statement)
                row = result.fetchone()
                print(row)
            sql_crud_obj = sql_crud()
            row = sql_crud_obj.returning_specific_row(engine, salva_table, data)
            print(row)
            return "row is deleted successfully"
        else:
            logger.info("this id is not present,so deletion is not successful")
            return "This id is not present"

    def delete_table(self, engine, salva_table):
        sql_crud_obj = sql_crud()
        sql_crud_obj.to_delete_table(engine, salva_table)
        logger.info("deleted the entire table")
        return "table deleted successfully"
