__author__ = 'bene'

import os
import pygame
from source.model.base.ViewingDirection import ViewingDirection


class Bullet(pygame.sprite.Sprite):

    def __init__(self, startTile, targetTile, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("resources", "images", "hero", "bullet.png"))
        self.rect = self.image.get_rect()
        self.rect.x = startTile.rect.x
        self.rect.y = startTile.rect.y
        self.targetX = targetTile.rect.x
        self.targetY = targetTile.rect.y
        self.direction = direction
        self.velocity = 8

    def update(self):
        if self.direction is ViewingDirection.NORTH:
            if self.rect.y is not self.targetY:
                self.rect.y -= self.velocity
            else:
                self.kill()

        if self.direction is ViewingDirection.EAST:
            if self.rect.x is not self.targetX:
                self.rect.x += self.velocity
            else:
                self.kill()

        if self.direction is ViewingDirection.SOUTH:
            if self.rect.y is not self.targetY:
                self.rect.y += self.velocity
            else:
                self.kill()

        if self.direction is ViewingDirection.SOUTH:
            if self.rect.y is not self.targetY:
                self.rect.y += self.velocity
            else:
                self.kill()