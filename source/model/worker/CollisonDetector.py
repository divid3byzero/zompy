import pygame
import os
class CollisionDetector(object):

    def __init__(self, playerGroup, enemyGroup, bulletGroup, wallGroup):
        self.playerGroup = playerGroup
        self.enemyGroup = enemyGroup
        self.bulletGroup = bulletGroup
        self.wallGroup = wallGroup

    def checkCollisions(self):
        self.__checkPlayerZombieCollision()
        self.__checkZombieBulletCollision()
        self.__checkBulletWallCollision()

    def __checkPlayerZombieCollision(self):
        collisions = pygame.sprite.groupcollide(self.playerGroup, self.enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for _ in v:
                k.life -= 1

    def __checkZombieBulletCollision(self):
        collisions = pygame.sprite.groupcollide(self.bulletGroup, self.enemyGroup, True, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.hit()
                self.playerGroup.sprites()[0].score += 1
                print(self.playerGroup.sprites()[0].score)

    # TODO: Bild fuer Explosion
    def __checkBulletWallCollision(self):
        collisions = pygame.sprite.groupcollide(self.wallGroup, self.bulletGroup, False, False)
        for k, v in collisions.iteritems():
            for i in v:
                i.image = pygame.image.load(os.path.join("resources", "images", "hero", "explosion_1.png"))