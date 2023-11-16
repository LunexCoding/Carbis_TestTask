import os
from pathlib import Path

from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)


class FileSystem:
    def __init__(self):
        pass

    @staticmethod
    def exists(path):
        return Path(path).exists()

    @staticmethod
    def isEmpty(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if not path.is_dir():
            raise IsNotDirectoryException(path)
        if not len(os.listdir(path)) == 0:
            raise IsNotEmptyException(path)
        return True

    @staticmethod
    def makeDir(path, parents=False, recreate=False):
        path = Path(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if path.exists() and recreate is False:
            raise PathExistsException(path)
        if not path.exists() and parents is False:
            if not path.parents[0].exists() and parents is False:
                raise PathNotFoundException(path)
        path.mkdir(exist_ok=recreate, parents=parents)
        return True

    @staticmethod
    def remove(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    @classmethod
    def removeDir(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if not cls.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    @classmethod
    def removeTree(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                cls.removeTree(child)
        path.rmdir()
        return True
