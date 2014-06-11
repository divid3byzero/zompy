__author__ = 'Sebastian'

import sys

from pygame.locals import *

from Window import *
from source.model.world.Map import *
from source.model.theming.ZombieThemeFactory import ZombieThemeFactory
from source.model.theming.GrasslandsThemeFactory import GrasslandsThemeFactory
from source.model.worker.MapGenerator import MapGenerator
from source.algo.Pathfinder import Pathfinder
from source.model.base.ViewingDirection import ViewingDirection
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
        self.pathfinder = Pathfinder()
        self.renderMenu = True

    def start(self):
        while True:
            self.__handle_events()
            if self.renderMenu:
                self.__renderMenu()
            else:
                self.drawWorld()

            if self.player is not None:
                self.player.move()

            pygame.display.flip()
            self.clock.tick(30)

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

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                startTile = self.map.getTileByCoords(event.pos)
                self.pathfinder.find(startTile, self.map.getTileByCoords(self.player.rect.center), self.map)

            pressedKeys = pygame.key.get_pressed()

            if pressedKeys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

            if pressedKeys[pygame.K_UP]:
                nextTile = self.map.getTileByCoords((self.player.rect.x, self.player.rect.y - BaseTile.HEIGHT))
                if nextTile.isWalkable:
                    self.player.setTarget(nextTile)

            if pressedKeys[pygame.K_DOWN]:
                nextTile = self.map.getTileByCoords((self.player.rect.x, self.player.rect.y + BaseTile.HEIGHT))
                if nextTile.isWalkable:
                    self.player.setTarget(nextTile)

            if pressedKeys[pygame.K_RIGHT]:
                nextTile = self.map.getTileByCoords((self.player.rect.x + BaseTile.WIDTH, self.player.rect.y))
                if nextTile.isWalkable:
                    self.player.setTarget(nextTile)

            if pressedKeys[pygame.K_LEFT]:
                nextTile = self.map.getTileByCoords((self.player.rect.x - BaseTile.WIDTH, self.player.rect.y))
                if nextTile.isWalkable:
                    self.player.setTarget(nextTile)

            if pressedKeys[pygame.K_1]:
                if self.renderMenu is not False:
                    self.themeFactory = ZombieThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False

            if pressedKeys[pygame.K_2]:
                if self.renderMenu is not False:
                    self.themeFactory = GrasslandsThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False

            if pressedKeys[pygame.K_u]:
                print("Nummer: {0}".format((self.map.getTileByCoords(pygame.mouse.get_pos())).number))