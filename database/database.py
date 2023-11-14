import sqlite3

from settingsConfig import settingsConfig


class DatabaseConnection(object):
    def __init__(self):
        self.dbConn = None
        self.dbCursor = None
        self.__settings = dict(database=settingsConfig.DatabaseSettings["database"])

    def __enter__(self):
        self.dbConn = sqlite3.connect(**self.__settings)
        self.dbCursor = self.dbConn.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.dbCursor.close()
            self.dbConn.close()
        except AttributeError:
            return True

    def execute(self, sql, data=None):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        self.dbConn.commit()

    def getData(self, sql, data=None, all=False):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        if all:
            return self.dbCursor.fetchall()
        return self.dbCursor.fetchone()

    @property
    def connection(self):
        return self.dbConn


databaseSession = DatabaseConnection()
