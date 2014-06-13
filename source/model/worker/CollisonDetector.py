import pygame

class CollisionDetector(object):

    def __init__(self):
        pass

    def checkPlayerZombieCollision(self, playerGroup, enemyGroup):
        collisions = pygame.sprite.groupcollide(playerGroup, enemyGroup, False, False)
        for k, v in collisions.iteritems():
            for _ in v:
                k.life -= 1
                print(k.life)
