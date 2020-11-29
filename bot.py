from Player import *
from game_config import *

class Bot(Player):

    def __init__(self,tx,ty,x,speed,maxhealth,ennemy):
        pygame.sprite.Sprite.__init__(self)
        #self.texture=pygame.image.load(texture)
        self.ennemy=ennemy
        self.texture=Surface(PLAYER_W,PLAYER_H)
        self.rect=pygame.Rect(x,GameConfig.player_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        pygame.draw.rect(self.texture,(0,0,255),(self.rect.x,self.rect.y,GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        
        self.speed=speed
        self.maxhealth=maxhealth

    def stepLeft(self):
        self.rect.x-=self.speed

    def stepRight(self):
        self.rect.x+=self.speed

    def update(self):
        if self.ennemy.rect.x>self.rect.x:
            stepRight()
        else:
            stepLeft()