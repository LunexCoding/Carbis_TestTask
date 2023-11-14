from helpers.fileSystem import FileSystem
from settingsConfig import settingsConfig
from database.pipeline import DatabasePipeline
from .queries import SqlQueries as initializerQueries


class _Initializer:
    def __init__(self):
        ...

    def initializeFileSystem(self):
        FileSystem.makeDir()

    def initializeDatabase(self):
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(initializerQueries.applyingSettings)
        databaseCreationPipeline.run()


g_initializer = _Initializer()
