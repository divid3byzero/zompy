__author__ = 'Sebastian'
import random
import math
import pygame
from source.model.world.elements.MapElement import *
from source.model.base.ViewingDirection import ViewingDirection

class Map(object):

    def __init__(self, mapfile, themeFactory):
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
        return self.tiles[self.getNumberOfTile((x, y))]

    def getTileByNumber(self, number):
        return self.tiles[number]

    def getNumberOfTile(self, (x, y)):
        col = int(math.ceil(x / BaseTile.WIDTH))
        row = int(math.ceil(y / BaseTile.HEIGHT))
        return (row * self.amountHorizontal) + col

    def getWalkableTile(self):
        return random.choice(self.walkableTiles)

    def getSpawnPoint(self):
        return random.choice(self.spawnPoints)

    def getNeighbors(self, tile):
        neighbors = []
        for direction in ViewingDirection.getViewingDirections():
            neighborTile = self.getNextTile(tile.rect.center, direction)
            if neighborTile.isWalkable:
                neighbors.append(neighborTile)
        return neighbors

    def getNextTile(self, (x, y), viewingDirection):
        nextTiles = {
            ViewingDirection.NORTH: self.getTileByCoords((x, y - BaseTile.HEIGHT)),
            ViewingDirection.EAST: self.getTileByCoords((x + BaseTile.WIDTH, y)),
            ViewingDirection.SOUTH: self.getTileByCoords((x, y + BaseTile.HEIGHT)),
            ViewingDirection.WEST: self.getTileByCoords((x - BaseTile.WIDTH, y))
        }
        return nextTiles[viewingDirection]

    def __initTiles(self):
        for m in range(self.amountVertical):
            for n in range(self.amountHorizontal):
                tile = self.themeFactory.createThemeElement(self.mapfile[m][n])
                tile.setCoordinates(m, n)
                tile.number = (m * self.amountHorizontal) + n
                self.tiles.append(tile)
                self.sprites.add(tile)

    def __collectWalkableTiles(self):
        for tile in self.tiles:
            if tile.isWalkable:
                self.walkableTiles.append(tile)

    def __collectSpawnPoints(self):
        for tile in self.walkableTiles:
            if tile.isSpawnPoint:
                self.spawnPoints.append(tile)

    def __collectWallTiles(self):
        for tile in self.tiles:
            if not tile.isWalkable:
                self.wallTiles.append(tile)