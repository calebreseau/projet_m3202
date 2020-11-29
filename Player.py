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
        self.projs=[]
        self.projspeed=GameConfig.player_projspeed
        self.vx=GameConfig.player_vx
        self.init_specs()
        self.window=window

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
            if proj.lifetime<GameConfig.proj_lifetime:
                proj.update()
            else:
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
        self.window.blit(self.texture,(self.rect.x,self.rect.y))