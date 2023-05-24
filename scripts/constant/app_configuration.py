import configparser


class Conf:
    config_obj = configparser.RawConfigParser()
    config_obj.read('configuration/application.conf')

    SERVER_HOST = config_obj.get("SERVICE", "HOST")
    SERVER_PORT = config_obj.get("SERVICE", "PORT")

    MONGO_DB_URI = config_obj.get("MONGO_DB_CREDENTIALS", "URI_1")
    MONGO_DB_DATABASE = config_obj.get("MONGO_DB_CREDENTIALS", "DATABASE")
    MONGO_DB_COURSE_COLLECTION = config_obj.get("MONGO_DB_CREDENTIALS", "COURSE_COLLECTION")
    MONGO_DB_STUDENT_COLLECTION = config_obj.get("MONGO_DB_CREDENTIALS", "STUDENT_COLLECTION")
