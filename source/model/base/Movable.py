__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta
from source.model.base.ViewingDirection import ViewingDirection
import pygame


class Movable(BaseTile):
    """
    Abstract base class for all movable objects (tiles) of the game
    """
    __metaclass__ = ABCMeta

    def __init__(self, image):
        """
        Constructor of the movable class
        :param image: the image of this tile
        """
        BaseTile.__init__(self, image)
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

    def move(self, velocityOverride=None):
        """
        Moves the tile by the given velocity
        :param velocityOverride: optional, can be used to change the moving speed
        """
        vel = self.velocity if velocityOverride is None else velocityOverride

        if self.targetX is not None and self.targetY is not None:
            if self.rect.x - self.targetX < 0:
                self._turn(ViewingDirection.EAST)
                self.rect.centerx += vel

            if self.rect.y - self.targetY < 0:
                self._turn(ViewingDirection.SOUTH)
                self.rect.centery += vel

            if self.rect.x - self.targetX > 0:
                self._turn(ViewingDirection.WEST)
                self.rect.centerx -= vel

            if self.rect.y - self.targetY > 0:
                self._turn(ViewingDirection.NORTH)
                self.rect.centery -= vel

            if self.rect.x - self.targetX is 0 and self.rect.y - self.targetY is 0:
                self.targetX, self.targetY = None, None

    def setTarget(self, nextTile):
        """
        Sets the target tile for the next step of the movable object
        :param nextTile: the next tile
        """
        if nextTile is not None and nextTile.isWalkable:
            if self.targetX is None and self.targetY is None:
                self.targetX = nextTile.rect.x
                self.targetY = nextTile.rect.y

    def __getTurningAngle(self, destination):
        """
        Gets the turning angle according to the current viewing direction and the destination tile
        :param destination: the destination tile
        :return: the needed turning angle
        """
        currentPos = self.possibleDestinations[self.viewingDirection]
        return currentPos[destination]

    def _turn(self, destination):
        """
        Turns the movable object
        :param destination: the destination of the movable
        """
        turningAngle = self.__getTurningAngle(destination)
        if turningAngle is not None:
            self.image = pygame.transform.rotate(self.image, turningAngle)
            self.viewingDirection = destination