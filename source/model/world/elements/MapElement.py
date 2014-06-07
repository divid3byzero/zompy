from source.model.base.BaseTile import BaseTile

__author__ = 'Sebastian'

import pygame


class MapElement(BaseTile):

    COLOR_WALKABLE = (128, 128, 128)
    COLOR_NOT_WALKABLE = (255, 0, 0)

    def __init__(self, col, row, walkable):
        BaseTile.__init__(self, col, row)
        self.isWalkable = walkable

    def draw(self, screen):
        if self.isWalkable:
            pygame.draw.rect(screen, MapElement.COLOR_WALKABLE, self)
        else:
            pygame.draw.rect(screen, MapElement.COLOR_NOT_WALKABLE, self)