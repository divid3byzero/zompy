__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


import pygame
import os
from pygame import font


class Window(object):
    """
    The game window
    """
    def __init__(self, width, height):
        """
        Constructor of the game window
        :param width: the width
        :param height: the height
        """
        pygame.display.set_caption("tiles")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menuElements = ["1: Zombies", "2: Grassland"]

    def renderMenu(self):
        """
        Renders the main menu
        """
        self.screen.fill((0,0,0))
        menuFont = font.Font(os.path.join("resources", "fonts", "PrintChar21.ttf"), 16)
        posX = self.screen.get_width() / 2
        vertOffset = 80
        for menuItem in self.menuElements:
            posY = self.screen.get_height() / 2 - vertOffset
            menuText = menuFont.render(menuItem, 1, (106, 227, 36))
            menuPosition = menuText.get_rect(centerx=posX, centery=posY)
            self.screen.blit(menuText, menuPosition)
            vertOffset -= menuText.get_rect().height + 10
