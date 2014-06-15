__author__ = 'bene'
import pygame
import os


class UserInterface(object):

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def draw(self):
        lifeBar = pygame.Rect(self.screen.get_rect().width - 120, 10, self.player.life, 15)
        pygame.draw.rect(self.screen, (106, 227, 36), lifeBar)

        menuFont = pygame.font.Font(os.path.join("resources", "fonts", "PrintChar21.ttf"), 14)
        menuText = menuFont.render(str(self.player.score), 1, (106, 227, 36))
        self.screen.blit(menuText, (self.screen.get_rect().x + 10, 10))

    def drawLostScreen(self):
        self.screen.fill((0, 0, 0))
        menuFont = pygame.font.Font(os.path.join("resources", "fonts", "PrintChar21.ttf"), 16)
        posX = self.screen.get_width() / 2
        posY = self.screen.get_height() / 2
        menuText = menuFont.render("You have lost. Please press key 'p' to continue...", 1, (106, 227, 36))
        menuPosition = menuText.get_rect(centerx=posX, centery=posY)
        self.screen.blit(menuText, menuPosition)