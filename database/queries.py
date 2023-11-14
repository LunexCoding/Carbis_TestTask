class SqlQueries:
    # DELETE A ROW FROM A TABLE #
    @staticmethod
    def deleteFromTable(tableName, targetElement, targetValue):
        return f"""
        DELETE FROM {tableName}
        WHERE {targetElement}={targetValue}
        """

    # UPDATE A ROW IN A TABLE #
    def updateTable(tableName, targetElement, targetValue, **kwargs):
        return f"""
        UPDATE {tableName}
        SET {", ".join([f"{key}=?" for key, value in kwargs.items()])}
        WHERE {targetElement}={targetValue}
        """

    # INSERT A ROW INTO THE REQUIRED TABLE #
    @staticmethod
    def insertIntoTable(tableName, *args):
        return f"""
            INSERT INTO {tableName}
            ({', '.join([char for char in args])})
            VALUES ({', '.join(["?" for char in args])})
        """

    # SELECT ROWS FROM TABLE #
    @staticmethod
    def selectFromTable(tableName, targetElement=None, targetValue=None, args=None):
        if targetElement == "*":
            return SqlQueries._selectAllFromTable(tableName)
        if targetElement and targetValue is not None:
            return SqlQueries._selectFromTableByWhere(tableName, targetElement, targetValue, args)
        return SqlQueries._selectFromTableByParams(tableName, args)

    # SELECT ROWS FROM THE REQUIRED TABLE #
    @staticmethod
    def _selectFromTableByParams(tableName, args):
        return f"""
        SELECT {', '.join([char for char in args])}
        FROM {tableName}
        """

    # SELECT ALL ROWS FROM THE REQUIRED TABLE #
    @staticmethod
    def _selectAllFromTable(tableName):
        return f"""
        SELECT * FROM {tableName}
        """

    @staticmethod
    def _selectFromTableByWhere(tableName, targetElement, targetValue, args):
        return f"""
        SELECT {', '.join([char for char in args])}
        FROM {tableName}
        WHERE {targetElement}={targetValue}
        """
