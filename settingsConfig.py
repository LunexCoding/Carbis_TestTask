from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfig = self.__loadSettings()

    def __loadSettings(self):
        __settings = {}
        __settings["DATABASE"] = dict(
            database=config("DB_NAME"),
        )
        __settings["FILE_SYSTEM"] = dict(
            fileSystem=config("DIRECTORIES_FOR_INITIALIZATION", cast=lambda v: [s.strip() for s in v.split(',')])
        )
        __settings["APP"] = None
        return __settings

    @property
    def databaseSettings(self):
        return self.__settingsConfig["DATABASE"]

    @property
    def fileSystemSettings(self):
        return self.__settingsConfig["FILE_SYSTEM"]

    @property
    def app(self):
        return self.__settingsConfig["APP"]

    @app.setter
    def app(self, settings):
        self.__settingsConfig["APP"] = settings


g_settingsConfig = _SettingsConfig()
