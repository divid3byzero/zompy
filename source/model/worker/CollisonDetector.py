__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import pygame

class CollisionDetector(object):
    """
    CollisionDetector for checking and handling all collision between the used spritegroups
    """
    def __init__(self, playerGroup, enemyGroup, bulletGroup, wallGroup):
        """
        Constructor of the collision detector
        :param playerGroup: the player spritegroup
        :param enemyGroup: the enemies spritegroup
        :param bulletGroup: the bullets spritegroup
        :param wallGroup: the walls spritegroup
        """
        self.playerGroup = playerGroup
        self.enemyGroup = enemyGroup
        self.bulletGroup = bulletGroup
        self.wallGroup = wallGroup

    def checkCollisions(self):
        """
        Checks the collisions
        """
        self.__checkPlayerZombieCollision()
        self.__checkZombieBulletCollision()
        self.__checkBulletWallCollision()

    def __checkPlayerZombieCollision(self):
        """
        Checks and handles the collisions between player and enemies
        """
        collisions = pygame.sprite.groupcollide(self.playerGroup, self.enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for _ in v:
                k.hit()

    def __checkZombieBulletCollision(self):
        """
        Checks and handles the collisions between enemies and bullets
        """
        collisions = pygame.sprite.groupcollide(self.bulletGroup, self.enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.hit()
                if i.hitpoints is 0:
                    self.playerGroup.sprites()[0].score += 1
                k.kill()

    def __checkBulletWallCollision(self):
        """
        Checks and handles the collisions between bullets and walls
        """
        collisions = pygame.sprite.groupcollide(self.wallGroup, self.bulletGroup, False, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.kill()