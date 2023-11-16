import httpx

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
            commands["help"]().execute(None)
        while True:
            try:
                com = input(Constants.COMMAND_PROMPT_MSG).split()
                command = com.pop(0)
                argCommand = " ".join(com)
                if command == "help" and len(argCommand) == 0:
                    argCommand = None
                if command in commands:
                    commands[command]().execute(argCommand)
                    if command == "set":
                        self.loadSettings()
                else:
                    print(Constants.UNKNOWN_COMMAND_MSG)
            except httpx.HTTPStatusError as e:
                print(Constants.HTTP_403_ERROR_MSG)
            except Exception as e:
                print(Constants.INPUT_ERROR_MSG)
            except KeyboardInterrupt:
                break
