__author__ = 'Sebastian'

import pygame
from pygame import locals


class Window(object):

    def __init__(self, width, height):
        pygame.display.set_caption("tiles")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

