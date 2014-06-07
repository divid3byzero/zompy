from source.model.objects.Player import Player

__author__ = 'Sebastian'

import sys
from pygame.locals import *
from Window import *
from source.model.world.Map import *
from source.model.worker.MapGenerator import MapGenerator
pygame.init()
class Controller(object):

    def __init__(self):
        self.mapfile = self.loadMap()
        self.map = Map(self.mapfile)
        self.window = Window(len(self.mapfile[0]) * BaseTile.WIDTH, len(self.mapfile) * BaseTile.HEIGHT)
        self.player = self.initPlayer()

    def start(self):
        while True:
            pygame.display.flip()
            self.drawWorld()
            self.__handle_events()

    def drawWorld(self):
        self.map.sprites.draw(self.window.screen)
        self.player.sprites.draw(self.window.screen)

    def loadMap(self):
        mapGenerator = MapGenerator()
        return mapGenerator.generateMap()

    def initPlayer(self):
        tile = self.map.getWalkableTile()
        return Player(tile.row, tile.col)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                print(self.map.getTileByCoords(event.pos[0], event.pos[1]))
