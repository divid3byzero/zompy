__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import pygame
import os

class Jukebox(object):
    """
    Class storing the background music of the game and controlling the playback.
    """
    def __init__(self):
        self.music = {"game" : pygame.mixer.Sound(os.path.join("resources", "sound", "zizibum.ogg")),
                      "dead" : pygame.mixer.Sound(os.path.join("resources", "sound", "smb_gameover.ogg")),
                      "menu" : pygame.mixer.Sound(os.path.join("resources", "sound", "cocktails_in_space.ogg"))}
        self.currentlyPlaying = None

    def playSound(self, sound):
        """
        Starts playback of the given sound if its not already playing.
        :param sound: the wanted sound
        """
        if sound is self.currentlyPlaying:
            pass
        else:
            if self.currentlyPlaying:
                self.music[self.currentlyPlaying].stop()
            if sound is "game":
                self.music[sound].play(loops = 1)
            else:
                self.music[sound].play()
            self.currentlyPlaying = sound