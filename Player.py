import pygame
from game_config import *
from Projectile import *

class Player(pygame.sprite.Sprite):    # player doit aussi posseder un set de vies (autre classe) et au moin une methode de tir.
    def __init__(self,kleft,kright,kshoot,window):
        pygame.sprite.Sprite.__init__(self)
        self.xlimit1=GameConfig.zonex1
        self.xlimit2=GameConfig.zonex2
        self.kleft=kleft
        self.kright=kright
        self.kshoot=kshoot
        self.shoot_cooldown=GameConfig.shoot_cooldown
        self.shoot_timer=0
        self.speed=GameConfig.playerspeed
        self.maxhealth=GameConfig.player_maxhealth
        self.health=self.maxhealth
        self.projs=[]
        self.projspeed=GameConfig.player_projspeed
        self.vx=GameConfig.player_vx
        self.texture=pygame.Surface((GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        pygame.draw.rect(self.texture,(80,80,80),(0,0,GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        self.init_specs()
        self.window=window

    def attack(self,power):
        self.health-=power
    
    def heal(self,power):
        self.health+=power

    def init_specs(self):
        self=self

    def shoot(self):
        if self.shoot_timer>self.shoot_cooldown:
            self.shoot_timer=0
            proj=Projectile(self,self.vx,self.vy,GameConfig.PROJ_SIZE,self.projspeed,self.window)
            self.projs.append(proj)
            

    def stepLeft(self):
        self.rect.x-=self.speed

    def stepRight(self):
        self.rect.x+=self.speed

    def update_projs(self):
        for proj in self.projs:
            proj.update()
            if proj.isdead:
                self.projs.remove(proj)

    def update(self):
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[self.kleft]:
            self.stepLeft()
        if keys[self.kright]:
            self.stepRight()
        if keys[self.kshoot]:
            self.shoot()
        self.update_projs()
        self.shoot_timer+=1
        self.draw()

    def draw(self):
        healthtexture=self.texture
        healthwidth=round(GameConfig.PLAYER_W*self.health/self.maxhealth)
        pygame.draw.rect(healthtexture,self.color,(0,0,healthwidth,GameConfig.PLAYER_H))
        pygame.draw.rect(healthtexture,(80,80,80),(healthwidth,0,GameConfig.PLAYER_W-healthwidth,GameConfig.PLAYER_H))
        #pygame.draw.rect(healthtexture,self.color,(0,0,32,GameConfig.PLAYER_H))
        self.window.blit(healthtexture,(self.rect.x,self.rect.y))