import sys

from dadata import Dadata

from .consts import Constants
from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables
from settingsConfig import g_settingsConfig


class FlagsType:
    SINGLE = 0
    WITH_VALUE = 1
    VALUE_WITHOUT_FLAG = 2


class ValueType:
    NONE = 0
    INT = 1
    STRING = 2


class Command:
    def __init__(self):
        self.msgHelp = None
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        assert False

    def getHelpMsg(self):
        return self.msgHelp

    def _getArgs(self, argsline):
        args = argsline.split()
        commandArgs = {}
        last = None
        flags = iter(self._argsWithoutFlagsOrder)
        for arg in args:
            if last is None:
                if arg in self._allowedFlags:
                    commandArgs[arg] = None
                    if self._allowedFlags[arg] != ValueType.NONE:
                        last = arg
                else:
                    last = next(flags)
                    commandArgs[last] = self._convertValue(last, arg)
                    last = None
            else:
                commandArgs[last] = self._convertValue(last, arg)
                last = None
        if last is not None:
            print("Invalid command")
        return commandArgs

    def _convertValue(self, flag, arg):
        valueType = self._allowedFlags[flag]
        if valueType == ValueType.INT:
            return int(arg)
        return arg


class Help(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.HELP_MSG
        self._allowedFlags = None
        self._argsWithoutFlagsOrder = None

    def execute(self, commandName=None):
        if commandName is None:
            print(self.msgHelp % "\n".join([f"\t{index}. {command}" for index, command in enumerate(commands, start=1)]))
        if commandName in commands:
            print(commands[commandName]().getHelpMsg())


class Quit(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.QUIT_HELP_MSG
        self._allowedFlags = None
        self._argsWithoutFlagsOrder = None

    def execute(self, argsLine=None):
        sys.exit()


class ShowSettings(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.SETTINGS_HELP_MSG
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        args = self._getArgs(args)
        with databaseSession as db:
            data = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement="*"), desc=True
            )
        for option, value in data.items():
            print(f"{option}: {value}")


class SetSettings(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.SET_HELP_MSG
        self._allowedFlags = {
            "-o": ValueType.STRING,
            "-v": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-o", "-v"]
        self._operations = {}

    def execute(self, args):
        args = self._getArgs(args)
        option = args["-o"]
        value = args["-v"]
        with databaseSession as db:
            oldValue = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement=option, args=[option]),
            )[0]
            db.execute(
                SqlQueries.updateTable(DatabaseTables.SETTINGS, option, option, oldValue), data=[value]
            )


class AddressSearch(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.ADDRESS_SEARCH_HELP_MSG
        self._allowedFlags = {
            "-a": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-a"]

    def execute(self, args):
        dadata = Dadata(g_settingsConfig.api)
        result = dadata.suggest("address", args, language=g_settingsConfig.language)
        return result


class ChooseAddress(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.CHOOSE_ADDRESS_HELP_MSG
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        addresses = {index: address["value"] for index, address in enumerate(args, start=1)}
        print(Constants.SUGGESTED_ADDRESSES_MSG)
        for index, address in addresses.items():
            print(f"\t{index}. {address}")
        indexRequiredAddress = int(input(Constants.ENTERING_INDEX_REQUIRED_ADDRESS_MSG))
        return addresses[indexRequiredAddress]


class FindAddressCoordinates(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.FIND_ADDRESS_COORDINATES_HELP_MSG
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        dadata = Dadata(g_settingsConfig.api)
        result = dadata.suggest("address", args, language=g_settingsConfig.language, count=1)
        return [result[0]["data"]["geo_lat"], result[0]["data"]["geo_lon"]]


class SearchPickAddressCoords(Command):
    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.SEARCH_PICK_ADDRESS_COORDS_HELP_MSG
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        addresses = AddressSearch().execute(args)
        if addresses:
            requiredAddress = ChooseAddress().execute(addresses)
            coords = FindAddressCoordinates().execute(requiredAddress)
            print(Constants.SELECTED_ADDRESS_MSG % requiredAddress)
            print(Constants.ADDRESS_COORDINATES_MSG % (coords[0], coords[1]))
        else:
            print(Constants.NOT_FOUND_ADDRESSES)


commands = {
    "settings": ShowSettings,
    "set": SetSettings,
    "help": Help,
    "q": Quit,
    "/s": SearchPickAddressCoords
}
