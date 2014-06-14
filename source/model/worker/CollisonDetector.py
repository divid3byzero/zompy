import pygame

class CollisionDetector(object):

    def __init__(self):
        pass

    def checkCollisions(self, playerGroup, enemyGroup, bulletGroup):
        self.__checkPlayerZombieCollision(playerGroup, enemyGroup)
        self.__checkZombieBulletCollision(bulletGroup, enemyGroup)

    def __checkPlayerZombieCollision(self, playerGroup, enemyGroup):
        collisions = pygame.sprite.groupcollide(playerGroup, enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for _ in v:
                k.life -= 1

    def __checkZombieBulletCollision(self, bulletGroup, enemyGroup):
        collisions = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.hit()

    def __checkBulletWallCollision(self, wallGroup, bulletGroup):
        collisions = pygame.sprite.groupcollide(wallGroup, bulletGroup, False, True)
