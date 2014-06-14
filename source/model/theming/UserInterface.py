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