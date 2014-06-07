__author__ = 'Sebastian'

from source.base.BaseTile import BaseTile
from abc import ABCMeta, abstractmethod

class Movable(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, row, col):
        BaseTile.__init__(self, row, col)

    @abstractmethod
    def moveNorth(self):
        pass

    @abstractmethod
    def moveEast(self):
        pass

    @abstractmethod
    def moveSouth(self):
        pass

    @abstractmethod
    def moveWest(self):
        pass