__author__ = 'Sebastian'

import sys

from pygame.locals import *

from Window import *
from source.model.world.Map import *
from source.model.theming.ZombieThemeFactory import ZombieThemeFactory
from source.model.theming.GrasslandsThemeFactory import GrasslandsThemeFactory
from source.model.worker.MapGenerator import MapGenerator

pygame.init()
class Controller(object):

    def __init__(self):
        self.themeFactory = None
        self.mapFile = self.loadMap()
        self.map = None
        self.window = Window(len(self.mapFile[0]) * BaseTile.WIDTH, len(self.mapFile) * BaseTile.HEIGHT)
        self.player = None
        self.clock = pygame.time.Clock()
        self.zombies = pygame.sprite.RenderPlain()
        self.renderMenu = True

    def start(self):
        while True:
            self.__handle_events()
            if self.renderMenu:
                self.__renderMenu()
            else:
                self.drawWorld()
            pygame.display.flip()

    def drawWorld(self):
        self.map.sprites.draw(self.window.screen)
        self.player.sprites.draw(self.window.screen)

    def loadMap(self):
        mapGenerator = MapGenerator()
        return mapGenerator.generateMap()

    def __initPlayer(self):
        tile = self.map.getWalkableTile()
        player = self.themeFactory.createThemeElement("pl")
        player.setCoordinates(tile.row, tile.col)
        return player

    def __renderMenu(self):
        self.window.renderMenu()

    def __initGameTheme(self):
        self.map = Map(self.mapFile, self.themeFactory)
        self.player = self.__initPlayer()

    def __handle_events(self):
        self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                print(self.map.getTileByCoords(event.pos).rect)
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
                if event.key == K_1:
                    self.themeFactory = ZombieThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False
                if event.key == K_2:
                    self.themeFactory = GrasslandsThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False
