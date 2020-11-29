import pygame
from game_config import *

class Player(pygame.sprite.Sprite):    # player doit aussi posseder un set de vies (autre classe) et au moin une methode de tir.
    def __init__(self,tx,ty,x,speed,maxhealth):
        pygame.sprite.Sprite.__init__(self)
        self.texture=pygame.Surface((GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        pygame.draw.rect(self.texture,(255,0,0),(0,0,GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        self.rect=pygame.Rect(x,GameConfig.player_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        
        self.speed=speed
        self.maxhealth=maxhealth

    def stepLeft(self):
        self.rect.x-=self.speed

    def stepRight(self):
        self.rect.x+=self.speed