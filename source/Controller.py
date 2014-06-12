import pygame

__author__ = 'Sebastian'

import sys

from pygame.locals import *

from Window import *
from source.model.world.Map import *
from source.model.theming.ZombieThemeFactory import ZombieThemeFactory
from source.model.theming.GrasslandsThemeFactory import GrasslandsThemeFactory
from source.model.worker.MapGenerator import MapGenerator
from source.model.objects.Enemy import Enemy
from source.algo.Pathfinder import Pathfinder
from source.model.base.ViewingDirection import ViewingDirection

pygame.init()

class Controller(object):

    def __init__(self):
        self.themeFactory = None
        self.mapFile = self.__loadMap()
        self.map = None
        self.window = Window(len(self.mapFile[0]) * BaseTile.WIDTH, len(self.mapFile) * BaseTile.HEIGHT)
        self.player = None
        self.clock = pygame.time.Clock()
        self.enemies = pygame.sprite.RenderPlain()
        self.pathfinder = Pathfinder()
        self.renderMenu = True

    def start(self):
        while True:
            self.__handle_events()
            if self.renderMenu:
                self.__renderMenu()
            else:
                self.__drawWorld()

            if self.player is not None:
                self.player.move()

            pygame.display.flip()
            self.clock.tick(30)

    def __drawWorld(self):
        self.map.sprites.draw(self.window.screen)
        self.player.sprites.draw(self.window.screen)
        self.enemies.draw(self.window.screen)

    def __loadMap(self):
        mapGenerator = MapGenerator()
        return mapGenerator.generateMap()

    def __initPlayer(self):
        tile = self.map.getWalkableTile()
        player = self.themeFactory.createThemeElement("pl")
        player.setCoordinates(tile.row, tile.col)
        return player

    def __initEnemies(self):
        tile = self.map.getWalkableTile()
        enemy = Enemy()
        enemy.setCoordinates(tile.row, tile.col)
        self.enemies.add(enemy)

    def __renderMenu(self):
        self.window.renderMenu()

    def __initGameTheme(self):
        self.map = Map(self.mapFile, self.themeFactory)
        self.player = self.__initPlayer()
        self.__initEnemies()

    def __handle_events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                self.enemies.update(self.player.rect.center, self.map)

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