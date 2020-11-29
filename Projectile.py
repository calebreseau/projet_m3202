import pygame
from game_config import *

class Projectile(pygame.sprite.Sprite) :
    def __init__(self, player, vx, vy, Size, Speed,window) :
        pygame.sprite.Sprite.__init__(self)
        self.isdead=False
        self.window=window
        self.lifetime=0
        self.rect=pygame.Rect(player.rect.x,player.rect.y,Size,Size)
        self.VX = vx
        self.VY = vy
        self.size = Size
        self.speed = Speed
        self.texture=pygame.Surface((Size,Size))
        pygame.draw.rect(self.texture,(255,255,255),(0,0,Size,Size))

    def update(self) :
        self.move()
        self.draw()
        self.lifetime+=1
        if self.lifetime>GameConfig.proj_lifetime:
            self.isdead=True

    def move(self) :
        self.rect.x += self.VX * self.speed
        self.rect.y += self.VY * self.speed

    def draw(self) :
        self.window.blit(self.texture, (self.rect.x,self.rect.y))



