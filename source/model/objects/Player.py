__author__ = 'Sebastian'

import pygame
from source.model.base.Movable import Movable


class Player(Movable):

    COLOR = (0, 255, 0)

    def __init__(self, row, col):
        Movable.__init__(self, row, col)

    def draw(self, screen):
        pygame.draw.rect(screen, Player.COLOR, self)