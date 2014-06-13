__author__ = 'bene'

import os
import pygame
from source.model.base.ViewingDirection import ViewingDirection
from source.model.base.Movable import Movable


class Bullet(Movable):

    image = pygame.image.load(os.path.join("resources", "images", "hero", "bullet.png"))

    def __init__(self, startTile, direction):
        Movable.__init__(self, self.image)
        self.rect = self.image.get_rect()
        self.rect.x = startTile.rect.x
        self.rect.y = startTile.rect.y
        self.targetX, self.targetY = None, None
        self.direction = direction
        self.velocity = 12

    def update(self):
        self.move()

    def move(self, velocityOverride=None):
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