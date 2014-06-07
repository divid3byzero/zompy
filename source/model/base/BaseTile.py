__author__ = 'Hanna'

import pygame
from abc import ABCMeta, abstractmethod

class BaseTile(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    def __init__(self, row, col, image):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = col * self.rect.width
        self.rect.y = row * self.rect.height