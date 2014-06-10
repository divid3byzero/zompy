__author__ = 'Sebastian'

import sys
from pygame.locals import *
from Window import *
from source.model.world.Map import *
from source.model.theming.ZombieThemeFactory import ZombieThemeFactory
from source.model.worker.MapGenerator import MapGenerator
from algo.pathfinding import aStar

pygame.init()
class Controller(object):

    def __init__(self):
        self.themeFactory = ZombieThemeFactory()
        mapFile = self.loadMap()
        self.map = Map(mapFile, self.themeFactory)
        self.window = Window(len(mapFile[0]) * BaseTile.WIDTH, len(mapFile) * BaseTile.HEIGHT)
        self.player = self.initPlayer()
        self.clock = pygame.time.Clock()
        self.zombies = pygame.sprite.RenderPlain()

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
        player = self.themeFactory.createThemeElement("pl")
        player.setCoordinates(tile.row, tile.col)
        return player

    def __handle_events(self):
        self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                aStar(self.map.getTileByCoords((event.pos)), self.map.getTileByCoords(self.player.rect.center), self.map)
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