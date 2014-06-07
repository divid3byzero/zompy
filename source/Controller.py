__author__ = 'Sebastian'

import pygame
from pygame import locals
from Window import *
from world.Map import *
pygame.init()

class Controller(object):

    def __init__(self):
        self.mapfile = self.loadMap()
        self.map = Map(self.mapfile)
        self.window = Window(len(self.mapfile[0]) * Tile.WIDTH, len(self.mapfile) * Tile.HEIGHT)
        # self.player = Player()

    def start(self):
        self.drawMap()
        pygame.display.flip()

    def drawMap(self):
        for row in self.map.tiles:
            for tile in row:
                tile.draw(self.window.screen)

    def loadMap(self):
        return [
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               ]