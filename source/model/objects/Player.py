__author__ = 'Sebastian'

import pygame
import os
from source.model.base.Movable import Movable


class Player(Movable):

    IMAGE = pygame.image.load(os.path.join("resources", "images", "objects", "zombie.png"))

    def __init__(self, row, col):
        Movable.__init__(self, row, col, Player.IMAGE)
        self.sprites = pygame.sprite.RenderPlain()
        self.sprites.add(self)