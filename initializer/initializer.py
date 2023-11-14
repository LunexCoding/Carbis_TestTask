from helpers.fileSystem import FileSystem
from settingsConfig import g_settingsConfig
from database.pipeline import DatabasePipeline
from database.queries import SqlQueries
from database.tables import DatabaseTables
from database.database import databaseSession
from .queries import SqlQueries as SqlInitializerQueries
from .consts import Constants


class _Initializer:
    def run(self):
        if not FileSystem.exists(Constants.DATA_DIRECTORY):
            self.initializeFileSystem()
            self.initializeDatabase()
            self.requestAndSaveSettings()

    @staticmethod
    def initializeFileSystem():
        for directory in g_settingsConfig.fileSystemSettings["fileSystem"]:
            FileSystem.makeDir(directory, recreate=True)

    @staticmethod
    def initializeDatabase():
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(SqlInitializerQueries.createTableSettings)
        databaseCreationPipeline.run()

    @staticmethod
    def requestAndSaveSettings():
        print(Constants.REQUEST_AND_SAVE_SETTINGS_MSG)
        while True:
            language = input("Language (en/ru) -> ")
            if language in ["en", "ru"]:
                break
            else:
                print("Выберите из en/ru")
        api = input("API KEY -> ")
        while True:
            try:
                helpStringVisibility = int(input("HelpStringVisibility (0/1) -> "))
                if helpStringVisibility in [0, 1]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Выберите из 0/1")
        with databaseSession as db:
            db.execute(
                SqlQueries.insertIntoTable(DatabaseTables.SETTINGS, "ServiceURL", "API", "Language", "HelpStringVisibility"),
                data=[Constants.SERVICE_URL, api, language, helpStringVisibility]
            )


g_initializer = _Initializer()
