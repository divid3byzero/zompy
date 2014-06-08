__author__ = 'Sebastian'

import pygame
import os
from source.model.base.Movable import Movable


class Enemy(Movable):

    IMAGE = pygame.image.load(os.path.join("resources", "images", "objects", "enemy.png"))

    def __init__(self, row, col):
        Movable.__init__(self, row, col, Enemy.IMAGE)
