import pygame
from game_config import *

class Player(pygame.sprite.Sprite):    # player doit aussi posseder un set de vies (autre classe) et au moin une methode de tir.
    def __init__(self,texture,tx,ty,x,speed,maxhealth):
        pygame.sprite.Sprite.__init__(self)
        self.texture=pygame.image.load(texture)
        self.rect=pygame.Rect(x,GameConfig.player_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        
        self.speed=speed
        self.maxhealth=maxhealth

    def stepLeft():
        self.pos.x-=1

    def stepRight():
        self.pos.x+=1