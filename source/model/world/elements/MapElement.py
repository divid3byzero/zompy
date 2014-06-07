from source.model.base.BaseTile import BaseTile

__author__ = 'Sebastian'

import pygame
import os

class MapElement(BaseTile):

    IMAGE_WALKABLE = pygame.image.load(os.path.join("resources", "images", "map", "mud.png"))
    IMAGE_NOT_WALKABLE = pygame.image.load(os.path.join("resources", "images", "map", "wall.png"))

    def __init__(self, col, row, walkable):
        if walkable:
            BaseTile.__init__(self, col, row, MapElement.IMAGE_WALKABLE)
        else:
            BaseTile.__init__(self, col, row, MapElement.IMAGE_NOT_WALKABLE)
        self.isWalkable = walkable