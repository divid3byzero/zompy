__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import pygame
import os


class UserInterface(object):
    """
    Class representing the user interface of the game
    """
    def __init__(self, screen, player):
        """
        Constructor of the user interface
        :param screen: the surface of the game
        :param player: the current player object
        """
        self.screen = screen
        self.player = player

    def draw(self):
        """
        Draws the user interface
        """
        lifeBar = pygame.Rect(self.screen.get_rect().width - 120, 10, self.player.life, 15)
        pygame.draw.rect(self.screen, (106, 227, 36), lifeBar)
        menuFont = pygame.font.Font(os.path.join("resources", "fonts", "PrintChar21.ttf"), 14)
        menuText = menuFont.render(str(self.player.score), 1, (106, 227, 36))
        self.screen.blit(menuText, (self.screen.get_rect().x + 10, 10))

    def drawLostScreen(self):
        """
        Draws the "game over screen"
        """
        self.screen.fill((0, 0, 0))
        menuFont = pygame.font.Font(os.path.join("resources", "fonts", "PrintChar21.ttf"), 16)
        posX = self.screen.get_width() / 2
        posY = self.screen.get_height() / 2
        menuTextFirst = menuFont.render("You have lost.", 1, (106, 227, 36))
        menuTextSecond = menuFont.render("Please press key 'p' to continue.", 1, (106, 227, 36))
        menuTextFirstPosition = menuTextFirst.get_rect(centerx=posX, centery=posY)
        menuTextSecondPosition = menuTextSecond.get_rect(centerx=posX, centery=posY + 30)
        self.screen.blit(menuTextFirst, menuTextFirstPosition)
        self.screen.blit(menuTextSecond, menuTextSecondPosition)