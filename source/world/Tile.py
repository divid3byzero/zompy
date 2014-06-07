__author__ = 'Sebastian'
import pygame
from pygame import locals


class Tile(pygame.Rect):

    WIDTH = 40
    HEIGHT = 40
    COLOR_WALKABLE = (128, 128, 128)
    COLOR_NOT_WALKABLE = (255, 0, 0)

    def __init__(self, col, row, walkable):
        self.walkable = walkable
        self.x = col * Tile.WIDTH
        self.y = row * Tile.HEIGHT
        pygame.Rect.__init__(self, self.x, self.y, Tile.WIDTH, Tile.HEIGHT)

    def draw(self, screen):
        if self.walkable:
            pygame.draw.rect(screen, Tile.COLOR_WALKABLE, self)
        else:
            pygame.draw.rect(screen, Tile.COLOR_NOT_WALKABLE, self)