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
        self.x += Movable.VELOCITY

    @abstractmethod
    def moveSouth(self):
        self.y += Movable.VELOCITY

    @abstractmethod
    def moveWest(self):
        self.x -= Movable.VELOCITY