import sqlite3
from lib import config

class Database:
    def __init__(self):
        conf = config.Conf()
        conf.read("main")

        self.__conn = sqlite3.connect(conf.get("database"))
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    def record_downtime(self, domain, status):
        pass

    def get_downtime(self, domain)
        pass
