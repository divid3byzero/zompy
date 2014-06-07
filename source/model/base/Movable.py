__author__ = 'Sebastian'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta, abstractmethod

class Movable(BaseTile):
    __metaclass__ = ABCMeta

    VELOCITY = 5

    def __init__(self, row, col):
        BaseTile.__init__(self, row, col)

    @abstractmethod
    def moveNorth(self):
        self.y -= Movable.VELOCITY

    @abstractmethod
    def moveEast(self):
        pass

    @abstractmethod
    def moveSouth(self):
        pass

    @abstractmethod
    def moveWest(self):
        pass