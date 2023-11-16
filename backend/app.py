from settingsConfig import g_settingsConfig
from initializer.initializer import g_initializer
from .commands import commands
from .consts import Constants
from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables


class App:
    def __init__(self):
        g_initializer.run()
        self.loadSettings()

    @staticmethod
    def loadSettings():
        with databaseSession as db:
            g_settingsConfig.app = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement="*"), desc=True
            )


    def run(self):
        if g_settingsConfig.app["HelpStringVisibility"] == 1:
            print(Constants.HELLO_MSG)
        while True:
            try:
                com = input("-> ").split()
                command = com.pop(0)
                argCommand = " ".join(com)
                if command == "help" and len(argCommand) == 0:
                    argCommand = None
                if command in commands:
                    commands[command].execute(argCommand)
                    if command == "set":
                        self.loadSettings()
                else:
                    print("Unknown command")
            except Exception as e:
                print(e)
                print("Input Error!")
                print("Use: help [command]")
            except KeyboardInterrupt:
                break
