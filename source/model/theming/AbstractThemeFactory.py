from twisted.protocols.amp import __metaclass__

__author__ = 'bene'

from abc import ABCMeta, abstractmethod
class AbstractThemeFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createThemeElement(self, elementType):
        pass