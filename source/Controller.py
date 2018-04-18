__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import sys

from pygame.locals import *

from Window import *
from model.world.Map import *
from model.theming.ZombieThemeFactory import ZombieThemeFactory
from model.theming.GrasslandsThemeFactory import GrasslandsThemeFactory
from model.worker.MapGenerator import MapGenerator
from model.worker.Jukebox import Jukebox
from model.worker.CollisonDetector import CollisionDetector
from model.objects.Enemy import Enemy
from model.objects.Bullet import Bullet
from algo.Pathfinder import Pathfinder
from model.base.ViewingDirection import ViewingDirection
from model.theming.UserInterface import UserInterface

pygame.init()


class Controller(object):
    """
    The Controller of the game
    """
    def __init__(self):
        """
        The Constructor of the Controller
        """
        self.themeFactory = None
        self.mapFile = self.__loadMap()
        self.map = None
        self.window = Window(len(self.mapFile[0]) * BaseTile.WIDTH, len(self.mapFile) * BaseTile.HEIGHT)
        self.jukebox = Jukebox()
        self.player = None
        self.clock = pygame.time.Clock()
        self.enemies = pygame.sprite.RenderPlain()
        self.bullets = pygame.sprite.RenderPlain()
        self.walls = pygame.sprite.RenderPlain()
        self.pathfinder = Pathfinder()
        self.players = pygame.sprite.RenderPlain()
        self.collisionDetector = None
        self.renderMenu = True
        self.userInterface = None

    def start(self):
        """
        Starts the game by "starting" the infinite loop
        :return:
        """
        self.jukebox.playSound("menu")
        while True:
            # PROCESS INPUT
            self.__handle_events()

            # LOGIC STUFF
            if self.renderMenu:
                self.jukebox.playSound("menu")
                self.__renderMenu()

            elif self.player.life <= 0:
                self.jukebox.playSound("dead")
                self.userInterface.drawLostScreen()


            else:
                self.jukebox.playSound("game")
                if self.player is not None:
                    self.player.move()

                if pygame.time.get_ticks() % (1000 / self.map.amountHorizontal) is 0:
                    self.__spawnEnemy()
                self.enemies.update(self.player, self.map)
                self.bullets.update()
                self.collisionDetector.checkCollisions()

                # DRAW EVERYTHING
                self.userInterface.draw()
                self.__drawWorld()

            pygame.display.flip()
            self.clock.tick(30)

    def __drawWorld(self):
        """
        Draws all game objects
        """
        self.map.sprites.draw(self.window.screen)
        self.players.draw(self.window.screen)
        self.enemies.draw(self.window.screen)
        self.bullets.draw(self.window.screen)
        self.userInterface.draw()

    def __loadMap(self):
        """
        Loads and generates the map
        :return: the generated map
        """
        mapGenerator = MapGenerator()
        return mapGenerator.generateMap()

    def __initPlayer(self):
        """
        Builds the Player
        :return: the player object
        """
        tile = self.map.getWalkableTile()
        player = self.themeFactory.createThemeElement("pl")
        player.setCoordinates(tile.row, tile.col)
        self.players.add(player)
        return player

    def __spawnEnemy(self):
        """
        Spawns the enemy at a random spawn point
        """
        tile = self.map.getSpawnPoint()
        enemy = Enemy()
        enemy.setCoordinates(tile.row, tile.col)
        self.enemies.add(enemy)

    def __renderMenu(self):
        """
        Renders the main menu
        """
        self.window.renderMenu()

    def __initGameTheme(self):
        """
        Sets up all needed objects to start the game
        :return:
        """
        self.map = Map(self.mapFile, self.themeFactory)
        self.player = self.__initPlayer()
        self.userInterface = UserInterface(self.window.screen, self.player)
        self.walls.add(self.map.wallTiles)
        self.collisionDetector = CollisionDetector(self.players, self.enemies, self.bullets, self.walls)

    def __reset(self):
        """
        Resets the game and all its objects
        :return:
        """
        self.map = None
        self.mapFile = self.__loadMap()
        self.window = Window(len(self.mapFile[0]) * BaseTile.WIDTH, len(self.mapFile) * BaseTile.HEIGHT)
        self.renderMenu = True
        self.enemies.empty()

    def __handle_events(self):
        """
        Handles all occuring events (pygame events)
        :return:
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shotSound.play()
                    bullet = Bullet(self.map.getTileByCoords(self.player.rect.center), self.player.viewingDirection)
                    self.bullets.add(bullet)

                if event.key == pygame.K_p:
                    if self.player.life <= 0:
                        self.__reset()

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)

        if self.renderMenu is False:
            if pressedKeys[pygame.K_UP]:
                self.player.setTarget(self.map.getNextTile(self.player.rect.center, ViewingDirection.NORTH))

            if pressedKeys[pygame.K_DOWN]:
                self.player.setTarget(self.map.getNextTile(self.player.rect.center, ViewingDirection.SOUTH))

            if pressedKeys[pygame.K_RIGHT]:
                self.player.setTarget(self.map.getNextTile(self.player.rect.center, ViewingDirection.EAST))

            if pressedKeys[pygame.K_LEFT]:
                self.player.setTarget(self.map.getNextTile(self.player.rect.center, ViewingDirection.WEST))

        if self.renderMenu is True:
            if pressedKeys[pygame.K_1]:
                self.themeFactory = ZombieThemeFactory()
                self.__initGameTheme()
                self.renderMenu = False

            if pressedKeys[pygame.K_2]:
                self.themeFactory = GrasslandsThemeFactory()
                self.__initGameTheme()
                self.renderMenu = False
