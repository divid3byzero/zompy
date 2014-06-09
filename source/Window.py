__author__ = 'Sebastian'

import pygame
import os
from pygame import font
class Window(object):

    def __init__(self, width, height):
        pygame.display.set_caption("tiles")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menuElements = ["1: Zombies", "2: Other"]

    def renderMenu(self):

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
