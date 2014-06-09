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
        # self.tiles = [[None for i in range(self.amountHorizontal)] for j in range(self.amountVertical)]
        self.tiles = []
        self.walkableTiles = []
        self.sprites = pygame.sprite.RenderPlain()
        self.__initTiles()

    def __initTiles(self):
        for m in range(self.amountVertical):
            for n in range(self.amountHorizontal):
                if self.mapfile[m][n] == 1:
                    tile = self.themeFactory.createWall()
                else:
                    tile = self.themeFactory.createFloor()
                    self.walkableTiles.append(tile)
                tile.setCoordinates(m, n)
                self.tiles.append(tile)
                self.sprites.add(tile)

    def getTileByCoords(self, (x ,y)):
        col = int(math.ceil(x / BaseTile.WIDTH))
        row = int(math.ceil(y / BaseTile.HEIGHT))
        number = (row * self.amountHorizontal) + col
        return self.tiles[number]

    def getWalkableTile(self):
        return random.choice(self.walkableTiles)