import sys

from .consts import Constants
from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables


class FlagsType:
    SINGLE = 0
    WITH_VALUE = 1
    VALUE_WITHOUT_FLAG = 2


class ValueType:
    NONE = 0
    INT = 1
    STRING = 2


class Command:
    def __init__(self, help):
        self.msgHelp = help
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, args):
        assert False

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
    def __init__(self, help):
        super().__init__(help)
        self._allowedFlags = None
        self._argsWithoutFlagsOrder = None

    def execute(self, commandName=None):
        if commandName is None:
            print(self.msgHelp)
        if commandName in commands:
            print(commands[commandName].msgHelp)


class Quit(Command):
    def __init__(self, help):
        super().__init__(help)
        self._allowedFlags = None
        self._argsWithoutFlagsOrder = None

    def execute(self, argsLine=None):
        sys.exit()


class ShowSettings(Command):
    def __init__(self, help):
        super().__init__(help)
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, argsLine):
        args = self._getArgs(argsLine)
        with databaseSession as db:
            data = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement="*"), desc=True
            )
        for option, value in data.items():
            print(f"{option}: {value}")


class SetSettings(Command):
    def __init__(self, help):
        super().__init__(help)
        self._allowedFlags = {
            "-o": ValueType.STRING,
            "-v": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-o", "-v"]
        self._operations = {}

    def execute(self, argsLine):
        args = self._getArgs(argsLine)
        option = args["-o"]
        value = args["-v"]
        with databaseSession as db:
            oldValue = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.SETTINGS, targetElement=option, args=[option]),
            )[0]
            db.execute(
                SqlQueries.updateTable(DatabaseTables.SETTINGS, option, option, oldValue), data=[value]
            )


commands = {
    "settings": ShowSettings(Constants.SETTINGS_HELP_MSG),
    "set": SetSettings(Constants.SET_HELP_MSG),
    'help': Help(Constants.HELP_MSG),
    'q': Quit(Constants.HELP_QUIT)
}
