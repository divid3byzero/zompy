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
        self.hitpoints = 1

    def update(self, player, map):
        target = self.pathfinder.find(map.getTileByCoords(self.rect.center), map.getTileByCoords(player.rect.center), map)
        self.setTarget(target)
        self.move(velocityOverride=2)

    def hit(self):
        self.hitpoints -= 1
        if self.hitpoints <= 0:
            self.kill()
