__author__ = 'bene'

from abc import ABCMeta, abstractmethod
from twisted.protocols.amp import __metaclass__
class AbstractThemeFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createThemeElement(self, elementIndicator):
        pass

    @abstractmethod
    def _createWall(self):
        pass
    @abstractmethod
    def _createFloor(self):
        pass

    @abstractmethod
    def _createPlayer(self):
        pass

