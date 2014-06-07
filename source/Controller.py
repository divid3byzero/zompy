from source.model.objects.Player import Player

__author__ = 'Sebastian'

import sys
from pygame.locals import *
from Window import *
from source.model.world.Map import *

pygame.init()
class Controller(object):

    def __init__(self):
        self.mapfile = self.loadMap()
        self.map = Map(self.mapfile)
        self.window = Window(len(self.mapfile[0]) * Tile.WIDTH, len(self.mapfile) * Tile.HEIGHT)
        self.player = self.initPlayer()


    def start(self):
        while True:
            self.drawMap()
            self.drawPlayer()
            pygame.display.flip()
            self.__handle_events()

    def drawMap(self):
        for row in self.map.tiles:
            for tile in row:
                tile.draw(self.window.screen)

    def drawPlayer(self):
        self.player.draw(self.window.screen)

    def loadMap(self):
        return [
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               ]

    def initPlayer(self):
        tile = self.map.getWalkableTile()
        return Player(tile.row, tile.col)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
