__author__ = 'Sebastian'

import pygame
from source.model.base.Movable import Movable


class Player(Movable):

    def __init__(self, pathToImage):
        Movable.__init__(self, pathToImage)
        self.sprites = pygame.sprite.RenderPlain()
        self.sprites.add(self)
        self.bullet = None

    def shoot(self):
        if self.bullet is not None:
            self.bullet.move(velocityOverride=10)