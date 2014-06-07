__author__ = 'Sebastian'

import sys
from pygame.locals import *
from Window import *
from source.model.objects.Player import Player
from source.model.world.Map import *

pygame.init()
class Controller(object):

    def __init__(self):
        self.mapfile = self.loadMap()
        self.map = Map(self.mapfile)
        self.window = Window(len(self.mapfile[0]) * 40, len(self.mapfile) * 40)
        # self.player = self.initPlayer()


    def start(self):
        while True:
            self.__handle_events()
            self.drawMap()
            # self.drawPlayer()
            pygame.display.flip()

    def drawMap(self):
        self.map.draw()

    def drawPlayer(self):
        self.player.draw(self.window.screen)

    def loadMap(self):
        return [
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
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
            # if event.type == KEYDOWN:
            #     if event.key == K_UP:
            #         print(self.player)
            #         self.player.moveNorth()
            #     if event.key == K_RIGHT:
            #         print(self.player)
            #         self.player.moveEast()
            #     if event.key == K_LEFT:
            #         print(self.player)
            #         self.player.moveWest()
            #     if event.key == K_DOWN:
            #         print(self.player)
            #         self.player.moveSouth()