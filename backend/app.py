from dadata import Dadata

from settingsConfig import g_settingsConfig
from initializer.initializer import g_initializer
from .commands import commands
from .consts import Constants
from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables


class App:
    def __init__(self):
        self.__settings = g_settingsConfig.app

        g_initializer.run()
        self.loadSettings()

    def loadSettings(self):
        with databaseSession as db:
            g_settingsConfig.app = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement="*"), desc=True
            )
            self.__settings = g_settingsConfig.app

    def run(self):
        if self.__settings["HelpStringVisibility"] == 1:
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
                else:
                    print("Unknown command")
            except Exception as e:
                print("Input Error!")
                print("Use: help [command]")
            except KeyboardInterrupt:
                break
