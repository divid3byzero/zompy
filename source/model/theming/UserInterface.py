__author__ = 'bene'
import pygame


class UserInterface(object):

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def draw(self):
        lifeBar = pygame.Rect(self.screen.get_rect().width - 120, 10, self.player.life, 15)
        pygame.draw.rect(self.screen, (0,250,0), lifeBar)