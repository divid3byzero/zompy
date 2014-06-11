__author__ = 'Sebastian'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta
from source.model.base.ViewingDirection import ViewingDirection
import pygame
class Movable(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, image):
        BaseTile.__init__(self, image, walkable=False)
        self.velocity = 4
        self.targetX = None
        self.targetY = None
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

    def move(self):

        if self.targetX is not None and self.targetY is not None:
            if self.rect.x - self.targetX < 0:
                self.__turn(ViewingDirection.EAST)
                self.rect.centerx += self.velocity

            if self.rect.y - self.targetY < 0:
                self.__turn(ViewingDirection.SOUTH)
                self.rect.centery += self.velocity

            if self.rect.x - self.targetX > 0:
                self.__turn(ViewingDirection.WEST)
                self.rect.centerx -= self.velocity

            if self.rect.y - self.targetY > 0:
                self.__turn(ViewingDirection.NORTH)
                self.rect.centery -= self.velocity

            if self.rect.x - self.targetX is 0 and self.rect.y - self.targetY is 0:
                self.targetX, self.targetY = None, None

    def setTarget(self, nextTile):

        if self.targetX is None and self.targetY is None:
            self.targetX = nextTile.rect.x
            self.targetY = nextTile.rect.y

    def __getTurningAngle(self, destination):

        currentPos = self.possibleDestinations[self.viewingDirection]
        return currentPos[destination]

    def __turn(self, destination):

        turningAngle = self.__getTurningAngle(destination)
        if turningAngle is not None:
            self.image = pygame.transform.rotate(self.image, turningAngle)
            self.viewingDirection = destination


