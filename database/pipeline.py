from .database import databaseSession


class DatabasePipeline:
    def __init__(self):
        self.__operations = []

    def addOperation(self, operation, data=None):
        self.__operations.append([operation, data])

    def run(self):
        with databaseSession as db:
            for operation in self.__operations:
                if operation[1] is not None:
                    db.execute(operation[0], operation[1])
                else:
                    db.execute(operation[0])
        self.__clear()

    def __clear(self):
        self.__operations.clear()
