__author__ = 'Sebastian'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta, abstractmethod

class Movable(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, row, col, image):
        BaseTile.__init__(self, row, col, image)

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