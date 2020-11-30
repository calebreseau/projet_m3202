import pygame
from game_config import *
from Projectile import *

class Player(pygame.sprite.Sprite):    # player doit aussi posseder un set de vies (autre classe) et au moin une methode de tir.
    
    def init_base(self,window):
        
        pygame.sprite.Sprite.__init__(self)
        self.xlimit1=GameConfig.zonex1
        self.xlimit2=GameConfig.zonex2
        
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
        self.window=window
        self.update=self.update_bot

    def init_human(self,kleft,kright,kshoot):
        self.kleft=kleft
        self.kright=kright
        self.kshoot=kshoot
        self.update=self.update_human


    def __init__(self,window,kleft=None,kright=None,kshoot=None):
        self.init_base(window)
        if (kleft!=None and kright!=None and kshoot!=None):
            self.init_human(kleft,kright,kshoot)

    def attack(self,power):
        self.health-=power
    
    def heal(self,power):
        self.health+=power

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
        self=self

    def update_human(self):
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

    def update_bot(self,ennemies):
        ennemy=ennemies[0]
        if ennemy.rect.x>self.rect.x:
            self.stepRight()
        else:
            self.stepLeft()
        self.draw()

    def update_collisions(self,ennemies):
            for proj in self.projs:
                for ennemy in ennemies:
                    print(str(ennemy.rect.x)+','+str(ennemy.rect.y))
                    if ennemy.rect.colliderect(proj.rect):
                        print('collide')
                        ennemy.attack(GameConfig.proj_damage)
                        print(str(ennemy.health))
                        self.projs.remove(proj)

    def draw(self):
        healthtexture=self.texture
        healthwidth=round(GameConfig.PLAYER_W*self.health/self.maxhealth)
        pygame.draw.rect(healthtexture,self.color,(0,0,healthwidth,GameConfig.PLAYER_H))
        pygame.draw.rect(healthtexture,(80,80,80),(healthwidth,0,GameConfig.PLAYER_W-healthwidth,GameConfig.PLAYER_H))
        #pygame.draw.rect(healthtexture,self.color,(0,0,32,GameConfig.PLAYER_H))
        self.window.blit(healthtexture,(self.rect.x,self.rect.y))