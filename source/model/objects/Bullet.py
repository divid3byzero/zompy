__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


import os
import pygame
from source.model.base.ViewingDirection import ViewingDirection
from source.model.base.Movable import Movable


class Bullet(Movable):
    """
    Represents the bullet which can be shot by the player
    """

    def __init__(self, startTile, direction):
        """
        Constructor of the bullet
        :param startTile: the start tile from where the bullet is fired
        :param direction: the "flying direction" of the bullet
        """
        self.image = pygame.image.load(os.path.join("resources", "images", "hero", "bullet_klein.png"))
        Movable.__init__(self, self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = startTile.rect.centerx
        self.rect.centery = startTile.rect.centery
        self.targetX, self.targetY = None, None
        self.direction = direction
        self.velocity = 12

    def update(self):
        """
        Used by spritegroups to update all contained sprites
        :return:
        """
        self.move()

    def move(self, velocityOverride=None):
        """
        Moves the bullet by the given velocity
        :param velocityOverride: optional, can be used to change the moving speed
        """
        if self.direction is ViewingDirection.NORTH:
            self._turn(ViewingDirection.NORTH)
            self.targetY = self.rect.y - 138
            if self.rect.y is not self.targetY:
                self.rect.y -= self.velocity

        if self.direction is ViewingDirection.EAST:
            self._turn(ViewingDirection.EAST)
            self.targetX = self.rect.x + 138
            if self.rect.x is not self.targetX:
                self.rect.x += self.velocity

        if self.direction is ViewingDirection.SOUTH:
            self._turn(ViewingDirection.SOUTH)
            self.targetY = self.rect.y + 138
            if self.rect.y is not self.targetY:
                self.rect.y += self.velocity

        if self.direction is ViewingDirection.WEST:
            self._turn(ViewingDirection.WEST)
            self.targetX = self.rect.x - 138
            if self.rect.x is not self.targetX:
                self.rect.x -= self.velocity