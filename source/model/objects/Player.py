__author__ = 'Sebastian'

import pygame
import os
from source.model.base.Movable import Movable


class Player(Movable):

    IMAGE = pygame.image.load(os.path.join("resources", "images", "zombie", "zombie.png"))

    def __init__(self, row, col):
        Movable.__init__(self, row, col, Player.IMAGE)
        self.sprites = pygame.sprite.RenderPlain()
        self.sprites.add(self)

    def moveNorth(self):
        pass

    def moveEast(self):
        pass

    def moveSouth(self):
        pass

    def moveWest(self):
        pass