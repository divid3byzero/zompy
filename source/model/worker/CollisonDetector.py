import pygame

class CollisionDetector(object):

    def __init__(self, playerGroup, enemyGroup, bulletGroup):
        self.playerGroup = playerGroup
        self.enemyGroup = enemyGroup
        self.bulletGroup = bulletGroup


    def checkCollisions(self):
        self.__checkPlayerZombieCollision()
        self.__checkZombieBulletCollision()

    def __checkPlayerZombieCollision(self):
        collisions = pygame.sprite.groupcollide(playerGroup, enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for _ in v:
                k.life -= 1

    def __checkZombieBulletCollision(self):
        collisions = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.hit()

    def __checkBulletWallCollision(self):
        collisions = pygame.sprite.groupcollide(wallGroup, bulletGroup, False, True)
