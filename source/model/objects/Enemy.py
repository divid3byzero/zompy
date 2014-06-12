__author__ = 'Sebastian'

import os
import pygame
from source.algo.Pathfinder import Pathfinder
from source.model.base.Movable import Movable


class Enemy(Movable):

    IMAGE = pygame.image.load(os.path.join("resources", "images", "zombie", "enemy.png"))

    def __init__(self):
        Movable.__init__(self, Enemy.IMAGE)
        self.pathfinder = Pathfinder()

    def update(self, playerCoords, map):
        step = self.pathfinder.find(map.getTileByCoords(self.rect.center), map.getTileByCoords(playerCoords), map)
        self.rect = step.rect