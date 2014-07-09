__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


import os
import pygame
from source.algo.Pathfinder import Pathfinder
from source.model.base.Movable import Movable


class Enemy(Movable):
    """
    Class representing the enemy.
    """
    def __init__(self):
        """
        Constructor of the enemy
        """
        self.image = pygame.image.load(os.path.join("resources", "images", "zombie", "enemy.png"))
        self.explosionSound = pygame.mixer.Sound(os.path.join("resources", "sound", "blast.ogg"))
        Movable.__init__(self, self.image)
        self.pathfinder = Pathfinder()
        self.hitpoints = 3
        self.removeIndex = False

    def update(self, player, map):
        """
        Used by spritegroups to update all contained sprites
        :param player: the player (used to get the current coordinates of the player)
        :param map: the played map
        """
        target = self.pathfinder.find(map.getTileByCoords(self.rect.center), map.getTileByCoords(player.rect.center), map)
        self.setTarget(target)
        self.move(velocityOverride=2)
        # Bugfix 09.07.2014
        # was: self.hitpoints = 0, caused enemies to stay alive although marked as dead
        if self.hitpoints <= 0:
            self.image = pygame.image.load(os.path.join("resources", "images", "hero", "explosion_1.png"))
            if self.removeIndex:
                self.kill()
                self.explosionSound.play()
            self.removeIndex = True

    def hit(self):
        """
        Called when the enemy is hit by a bullet. Reduces the enemies hitpoints.
        """
        self.hitpoints -= 1