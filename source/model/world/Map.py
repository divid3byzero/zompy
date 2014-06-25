__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import random
import math
import pygame
from source.model.world.elements.MapElement import *
from source.model.base.ViewingDirection import ViewingDirection

class Map(object):
    """
    Class representing the map of the game
    """
    def __init__(self, mapfile, themeFactory):
        """
        Constructor of the map class
        :param mapfile: the mapfile by which the map is created
        :param themeFactory: the theme factory for creating all needed map elements
        """
        self.mapfile = mapfile
        self.themeFactory = themeFactory
        self.amountHorizontal = len(mapfile[0])
        self.amountVertical = len(mapfile)
        self.tiles = []
        self.walkableTiles = []
        self.spawnPoints = []
        self.wallTiles = []
        self.sprites = pygame.sprite.RenderPlain()
        self.__initTiles()
        self.__collectWalkableTiles()
        self.__collectSpawnPoints()
        self.__collectWallTiles()

    def getTileByCoords(self, (x, y)):
        """
        Returns a tile by its coordinates
        :param (x,y): the coordinates of the wanted tile
        :return: the tile
        """
        return self.tiles[self.getNumberOfTile((x, y))]

    def getTileByNumber(self, number):
        """
        Returns a tile by its number
        :param number: the numberof the wanted tile
        :return: the tile at the specified index
        """
        return self.tiles[number]

    def getNumberOfTile(self, (x, y)):
        """
        Gets the Number of the tile at the specified coordinated
        :return: the tile at the specified coordinated
        """
        col = int(math.ceil(x / BaseTile.WIDTH))
        row = int(math.ceil(y / BaseTile.HEIGHT))
        return (row * self.amountHorizontal) + col

    def getWalkableTile(self):
        """
        Gets a random walkable tile
        :return: a random walkable tile
        """
        return random.choice(self.walkableTiles)

    def getSpawnPoint(self):
        """
        Returns a random spawnpoint
        :return: the spawnpoint
        """
        return random.choice(self.spawnPoints)

    def getNeighbors(self, tile):
        """
        Returns all neighbor tiles (North, East, South, West) of the passed tile
        :param tile: the tile whose surrounding tiles are searched
        :return: the surrounding tiles
        """
        neighbors = []
        for direction in ViewingDirection.getViewingDirections():
            neighborTile = self.getNextTile(tile.rect.center, direction)
            if neighborTile.isWalkable:
                neighbors.append(neighborTile)
        return neighbors

    def getNextTile(self, (x, y), viewingDirection):
        """
        Gets the next tile according to the viewing direction
        :param viewingDirection: the viewing direction
        :return: the next tile
        """
        nextTiles = {
            ViewingDirection.NORTH: self.getTileByCoords((x, y - BaseTile.HEIGHT)),
            ViewingDirection.EAST: self.getTileByCoords((x + BaseTile.WIDTH, y)),
            ViewingDirection.SOUTH: self.getTileByCoords((x, y + BaseTile.HEIGHT)),
            ViewingDirection.WEST: self.getTileByCoords((x - BaseTile.WIDTH, y))
        }
        return nextTiles[viewingDirection]

    def __initTiles(self):
        """
        Instantiates all tiles as specified in the mapfile
        :return:
        """
        for m in range(self.amountVertical):
            for n in range(self.amountHorizontal):
                tile = self.themeFactory.createThemeElement(self.mapfile[m][n])
                tile.setCoordinates(m, n)
                tile.number = (m * self.amountHorizontal) + n
                self.tiles.append(tile)
                self.sprites.add(tile)

    def __collectWalkableTiles(self):
        """
        Collects all walkable tiles in an extra list
        """
        for tile in self.tiles:
            if tile.isWalkable:
                self.walkableTiles.append(tile)

    def __collectSpawnPoints(self):
        """
        Collects all spawnpoints in an extra list
        """
        for tile in self.walkableTiles:
            if tile.isSpawnPoint:
                self.spawnPoints.append(tile)

    def __collectWallTiles(self):
        """
        Collects all non walkable tiles in an extra list
        """
        for tile in self.tiles:
            if not tile.isWalkable:
                self.wallTiles.append(tile)