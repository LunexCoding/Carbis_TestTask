import sqlite3

from settingsConfig import g_settingsConfig


class DatabaseConnection(object):
    def __init__(self):
        self.dbConn = None
        self.dbCursor = None
        self.__settings = dict(database=g_settingsConfig.databaseSettings["database"])

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

    def getData(self, sql, data=None, all=False, desc=False):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        if all:
            return self.dbCursor.fetchall()
        if desc:
            description = self.dbCursor.description
            columnNames = [col[0] for col in description]
            return [dict(zip(columnNames, row)) for row in self.dbCursor.fetchall()][0]
        return self.dbCursor.fetchone()

    @property
    def connection(self):
        return self.dbConn


databaseSession = DatabaseConnection()
