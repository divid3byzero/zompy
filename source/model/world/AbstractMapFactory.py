from twisted.protocols.amp import __metaclass__

__author__ = 'bene'

from abc import ABCMeta, abstractmethod
class AbstractMapFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createPlayer(self):
        pass

    @abstractmethod
    def createEnemy(self):
        pass

    @abstractmethod
    def createTile(self, elementType):
        pass