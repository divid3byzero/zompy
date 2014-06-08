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
        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            self.__handle_events()
            self.drawWorld()
            pygame.display.flip()

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
        self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                self.map.getTileByCoords(event.pos).rect
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    nextTile = self.map.getTileByCoords((self.player.rect.centerx, self.player.rect.centery - BaseTile.HEIGHT))
                    if nextTile.isWalkable:
                        self.player.moveNorth()
                if event.key == K_DOWN:
                    nextTile = self.map.getTileByCoords((self.player.rect.centerx, self.player.rect.centery + BaseTile.HEIGHT))
                    if nextTile.isWalkable:
                        self.player.moveSouth()
                if event.key == K_RIGHT:
                    nextTile = self.map.getTileByCoords((self.player.rect.centerx + BaseTile.WIDTH, self.player.rect.centery))
                    if nextTile.isWalkable:
                        self.player.moveEast()
                if event.key == K_LEFT:
                    nextTile = self.map.getTileByCoords((self.player.rect.centerx - BaseTile.WIDTH, self.player.rect.centery))
                    if nextTile.isWalkable:
                        self.player.moveWest()