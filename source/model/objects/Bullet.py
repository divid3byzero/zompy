__author__ = 'bene'

import pygame
import os
from source.model.base.Movable import Movable


class Bullet(Movable):

    image = pygame.image.load(os.path.join("resources", "images", "hero", "bullet.png"))

    def __init__(self):
        Movable.__init__(self, self.image)
        self.velocity = 12

    def move(self, velocityOverride=None):
        vel = self.velocity if velocityOverride is None else velocityOverride

        if self.targetX is not None and self.targetY is not None:
            if self.rect.x - self.targetX < 0:
                self.rect.centerx += vel

            if self.rect.y - self.targetY < 0:
                self.rect.centery += vel

            if self.rect.x - self.targetX > 0:
                self.rect.centerx -= vel

            if self.rect.y - self.targetY > 0:
                self.rect.centery -= vel

            if self.rect.x - self.targetX is 0 and self.rect.y - self.targetY is 0:
                self.targetX, self.targetY = None, None

    def update(self):
        self.move()
        if self.targetX is None and self.targetY is None:       
            self.kill()