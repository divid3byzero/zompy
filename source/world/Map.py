__author__ = 'Sebastian'
from Tile import *
from Window import *

class Map(object):


    def __init__(self, mapfile):
        self.mapfile = mapfile
        self.amountHorizontal = len(mapfile[0])
        self.amountVertical = len(mapfile)
        self.tiles = [[None for i in range(self.amountHorizontal)] for j in range(self.amountVertical)]
        self.walkableTiles = []
        self.__initTiles()

    def __initTiles(self):
        for n in range(self.amountVertical):
            for m in range(self.amountHorizontal):
                if self.mapfile[n][m] == 1:
                    tile = Tile(m, n, False)
                else:
                    tile = Tile(m, n, True)
                    self.walkableTiles.append(tile)
                self.tiles[n][m] = tile

    def getTileByCoords(self, x, y):
        col = x / Tile.WIDTH
        row = y / Tile.HEIGHT
        return self.tiles[row][col]