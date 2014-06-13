__author__ = 'bene'

from source.model.theming.AbstractThemeFactory import *

import os
import pygame
class ZombieThemeFactory(AbstractThemeFactory):

    def __init__(self):
        self.__walkableImage = pygame.image.load(os.path.join("resources", "images", "map", "mud.png"))
        self.__notWalkableImage = pygame.image.load(os.path.join("resources", "images", "map", "wall.png"))
        self.__spawnImage = pygame.image.load(os.path.join("resources", "images", "map", "spawn.png"))
        self.__playerImage = pygame.image.load(os.path.join("resources", "images", "zombie", "zombie.png"))

    def _createWall(self):
        return WallTile(self.__notWalkableImage)

    def _createFloor(self):
        return FloorTile(self.__walkableImage)

    def _createPlayer(self):
        return Player(self.__playerImage)

    def _createSpawnPoint(self):
        return FloorTile(self.__spawnImage, True)