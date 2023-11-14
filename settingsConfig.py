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
        return __settings

    @property
    def DatabaseSettings(self):
        return self.__settingsConfig["DATABASE"]

    @property
    def FileSystemSettings(self):
        return self.__settingsConfig["FILE_SYSTEM"]


settingsConfig = _SettingsConfig()
