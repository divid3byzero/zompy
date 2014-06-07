__author__ = 'Sebastian'
import random

from source.model.world.elements.MapElement import *


class Map(object):


    def __init__(self, mapfile):
        self.mapfile = mapfile
        self.amountHorizontal = len(mapfile[0])
        self.amountVertical = len(mapfile)
        self.tiles = [[None for i in range(self.amountHorizontal)] for j in range(self.amountVertical)]
        self.walkableTiles = []
        self.__initTiles()

    def __initTiles(self):
        for m in range(self.amountVertical):
            for n in range(self.amountHorizontal):
                if self.mapfile[m][n] == 1:
                    tile = MapElement(m, n, False)
                else:
                    tile = MapElement(m, n, True)
                    self.walkableTiles.append(tile)
                self.tiles[m][n] = tile

    def getTileByCoords(self, x, y):
        col = x / BaseTile.WIDTH
        row = y / BaseTile.HEIGHT
        return self.tiles[row][col]

    def getWalkableTile(self, row = None, col = None):
        if col is not None and row is not None:
            if self.tiles[row][col].isWalkable:
                return self.tiles[row][col]

        return random.choice(self.walkableTiles)

