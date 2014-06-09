__author__ = 'Sebastian'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta, abstractmethod
from source.model.base.ViewingDirection import ViewingDirection
import pygame


class Movable(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, pathToImage):
        BaseTile.__init__(self, pathToImage, walkable=False)
        self.viewingDirection = ViewingDirection.SOUTH
        self.possibleDestinations = {
            "north": {
                "north": None,
                "east": 270,
                "south": 180,
                "west": 90
            },
            "east": {
                "north": 90,
                "east": None,
                "south": 270,
                "west": 180
            },
            "south": {
                "north": 180,
                "east": 90,
                "south": None,
                "west": 270
            },
            "west": {
                "north": 270,
                "east": 180,
                "south": 90,
                "west": None
            }
        }

    def moveNorth(self):
        self.rect.y -= BaseTile.HEIGHT
        self.__turn(ViewingDirection.NORTH)

    def moveEast(self):
        self.rect.x += BaseTile.WIDTH
        self.__turn(ViewingDirection.EAST)

    def moveSouth(self):
        self.rect.y += BaseTile.HEIGHT
        self.__turn(ViewingDirection.SOUTH)

    def moveWest(self):
        self.rect.x -= BaseTile.WIDTH
        self.__turn(ViewingDirection.WEST)

    def __getTurningAngle(self, destination):
        currentPos = self.possibleDestinations[self.viewingDirection]
        return currentPos[destination]

    def __turn(self, destination):
        turningAngle = self.__getTurningAngle(destination)
        if turningAngle is not None:
            self.image = pygame.transform.rotate(self.image, turningAngle)
            self.viewingDirection = destination

