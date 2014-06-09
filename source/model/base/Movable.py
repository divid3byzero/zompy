__author__ = 'Sebastian'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta, abstractmethod

class Movable(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, pathToImage):
        BaseTile.__init__(self, pathToImage)

    def moveNorth(self):
        self.rect.y -= BaseTile.HEIGHT

    def moveEast(self):
        self.rect.x += BaseTile.WIDTH

    def moveSouth(self):
        self.rect.y += BaseTile.HEIGHT

    def moveWest(self):
        self.rect.x -= BaseTile.WIDTH
