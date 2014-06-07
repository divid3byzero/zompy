__author__ = 'Sebastian'

from source.base.Movable import Movable
import pygame

class Player(Movable):

    COLOR = (0, 255, 0)

    def __init__(self, row, col):
        Movable.__init__(self, row, col)

    def draw(self, screen):
        pygame.draw.rect(screen, Player.COLOR, self)