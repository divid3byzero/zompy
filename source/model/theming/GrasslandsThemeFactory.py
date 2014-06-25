__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'



from source.model.theming.AbstractThemeFactory import AbstractThemeFactory
from source.model.objects.Player import Player
from source.model.world.elements.FloorTile import FloorTile
from source.model.world.elements.WallTile import WallTile
import os
import pygame


class GrasslandsThemeFactory(AbstractThemeFactory):
    """
    Theme factory of the grassland-theme implementing the AbstractThemeFactory
    """
    def __init__(self):
        """
        Constructor of the factory
        """
        self.__walkableImage = pygame.image.load(os.path.join("resources", "images", "map", "grass.png"))
        self.__notWalkableImage = pygame.image.load(os.path.join("resources", "images", "map", "wall_grey.png"))
        self.__spawnImage = pygame.image.load(os.path.join("resources", "images", "map", "spawn.png"))
        self.__playerImage = pygame.image.load(os.path.join("resources", "images", "zombie", "femalezombie.png"))

    def _createWall(self):
        """
        Creates wall tiles of the grassland theme
        :return: the wall tile
        """
        return WallTile(self.__notWalkableImage)

    def _createFloor(self):
        """
        Creates floor tiles of the grassland theme
        :return: the floor tile
        """
        return FloorTile(self.__walkableImage)

    def _createPlayer(self):
        """
        Creates the player of the grassland theme
        :return: the player
        """
        return Player(self.__playerImage)

    def _createSpawnPoint(self):
        """
        Creates spawnpoint tiles of the grassland theme
        :return: the spawnpoint tile
        """
        return FloorTile(self.__spawnImage, True)
