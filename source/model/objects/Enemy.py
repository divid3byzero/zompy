__author__ = 'Sebastian'

import os
import pygame
from source.algo.Pathfinder import Pathfinder
from source.model.base.Movable import Movable


class Enemy(Movable):

    def __init__(self):
        self.image = pygame.image.load(os.path.join("resources", "images", "zombie", "enemy.png"))
        Movable.__init__(self, self.image)
        self.pathfinder = Pathfinder()
        self.hitpoints = 3
        self.removeIndex = False

    def update(self, player, map):
        target = self.pathfinder.find(map.getTileByCoords(self.rect.center), map.getTileByCoords(player.rect.center), map)
        self.setTarget(target)
        self.move(velocityOverride=2)
        if self.hitpoints is 0:
            self.image = pygame.image.load(os.path.join("resources", "images", "hero", "explosion_1.png"))
            if self.removeIndex:
                self.kill()
                pygame.mixer.Sound(os.path.join("resources", "sound", "blast.ogg")).play()
            self.removeIndex = True

    def hit(self):
        self.hitpoints -= 1