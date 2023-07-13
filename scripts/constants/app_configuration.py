import configparser


class Conf:
    config_obj = configparser.RawConfigParser()
    config_obj.read('configuration/application.conf')

    SERVER_HOST = config_obj.get("SERVICE", "HOST")
    SERVER_PORT = config_obj.get("SERVICE", "PORT")
