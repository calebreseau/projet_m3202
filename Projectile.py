import pygame
from game_config import *

class Projectile(pygame.sprite.Sprite) :
    def __init__(self, player, vx, vy, Size, Speed) :
        pygame.sprite.Sprite.__init__(self)
        X = player.pos.x
        Y = player.pos.y
        VX = vx
        VY = vy
        size = Size
        speed = Speed
    def update(self) :
        moove()
        draw()
    def moove(self) :
        X += VX * speed
        Y += VY * speed
    def draw(self) :
        self.fill("red")
        self.rect=pygame.Rect(X,Y,size,size)     #a modifier, utiliser des images



