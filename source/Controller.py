import pygame

__author__ = 'Sebastian'

import sys

from pygame.locals import *

from Window import *
from source.model.world.Map import *
from source.model.base.ViewingDirection import ViewingDirection
from source.model.theming.ZombieThemeFactory import ZombieThemeFactory
from source.model.theming.GrasslandsThemeFactory import GrasslandsThemeFactory
from source.model.worker.MapGenerator import MapGenerator
from source.model.worker.CollisonDetector import CollisionDetector
from source.model.objects.Bullet import Bullet
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
        self.collisionDetector = CollisionDetector()
        self.renderMenu = True

    def start(self):
        while True:
            if self.renderMenu:
                self.__renderMenu()
            else:
                self.__drawWorld()
                if self.player is not None:
                    self.player.move()
                    self.player.shoot()
                self.enemies.update(self.player, self.map)
                self.collisionDetector.checkPlayerZombieCollision(self.player.sprites, self.enemies)

            self.__handle_events()
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

    def __nextTile(self, viewingDirection):

        nextTile = None
        if viewingDirection is ViewingDirection.NORTH:
            nextTile = self.map.getTileByCoords((self.player.rect.x, self.player.rect.y - BaseTile.HEIGHT))

        if viewingDirection is ViewingDirection.EAST:
            nextTile = self.map.getTileByCoords((self.player.rect.x + BaseTile.WIDTH, self.player.rect.y))

        if viewingDirection is ViewingDirection.SOUTH:
            nextTile = self.map.getTileByCoords((self.player.rect.x, self.player.rect.y + BaseTile.HEIGHT))

        if viewingDirection is ViewingDirection.WEST:
            nextTile = self.map.getTileByCoords((self.player.rect.x - BaseTile.WIDTH, self.player.rect.y))

        return nextTile

    def __initEnemies(self):
        
        for _ in range(3):
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

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)

        if self.renderMenu is False:
            if pressedKeys[pygame.K_UP]:
                self.player.setTarget(self.__nextTile(ViewingDirection.NORTH))

            if pressedKeys[pygame.K_DOWN]:
                self.player.setTarget(self.__nextTile(ViewingDirection.SOUTH))

            if pressedKeys[pygame.K_RIGHT]:
                self.player.setTarget(self.__nextTile(ViewingDirection.EAST))

            if pressedKeys[pygame.K_LEFT]:
                self.player.setTarget(self.__nextTile(ViewingDirection.WEST))

            if pressedKeys[pygame.K_SPACE]:
                bullet = Bullet()
                bullet.setTarget(self.__nextTile(self.player.viewingDirection))
                self.player.bullet = bullet

        if self.renderMenu is True:
            if pressedKeys[pygame.K_1]:
                    self.themeFactory = ZombieThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False

            if pressedKeys[pygame.K_2]:
                    self.themeFactory = GrasslandsThemeFactory()
                    self.__initGameTheme()
                    self.renderMenu = False

