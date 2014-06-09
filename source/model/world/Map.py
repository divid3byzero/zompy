__author__ = 'Sebastian'
import random
import math
import pygame
from source.model.world.elements.MapElement import *

class Map(object):

    def __init__(self, mapfile, themeFactory):
        self.mapfile = mapfile
        self.themeFactory = themeFactory
        self.amountHorizontal = len(mapfile[0])
        self.amountVertical = len(mapfile)
        self.tiles = []
        self.walkableTiles = []
        self.sprites = pygame.sprite.RenderPlain()
        self.__initTiles()
        self.__collectWalkableTiles()

    def getTileByCoords(self, (x ,y)):
        return self.tiles[self.getNumberOfTile((x, y))]

    def getNumberOfTile(self, (x, y)):
        col = int(math.ceil(x / BaseTile.WIDTH))
        row = int(math.ceil(y / BaseTile.HEIGHT))
        return (row * self.amountHorizontal) + col

    def getWalkableTile(self):
        return random.choice(self.walkableTiles)

    def __initTiles(self):
        for m in range(self.amountVertical):
            for n in range(self.amountHorizontal):
                tile = self.themeFactory.createThemeElement(self.mapfile[m][n])
                tile.setCoordinates(m, n)
                self.tiles.append(tile)
                self.sprites.add(tile)

    def __collectWalkableTiles(self):
        for tile in self.tiles:
            if tile.isWalkable:
                self.walkableTiles.append(tile)