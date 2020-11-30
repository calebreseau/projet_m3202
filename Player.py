import pygame
from game_config import *
from Projectile import *
from Bonus import *

class Player(pygame.sprite.Sprite):    # player doit aussi posseder un set de vies (autre classe) et au moin une methode de tir.
    
    def assign(self,player):
        self=player

    def init_base(self,window):
        
        pygame.sprite.Sprite.__init__(self)
        self.effects=[]
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

    def init_human(self,kleft,kright,kshoot):
        self.kleft=kleft
        self.kright=kright
        self.kshoot=kshoot


    def __init__(self,window,kleft=None,kright=None,kshoot=None):
        self.init_base(window)
        if (kleft!=None and kright!=None and kshoot!=None):
            self.init_human(kleft,kright,kshoot)

    def attack(self,power):
        self.health-=power
    
    def heal(self,power):
        self.health+=power
        if self.health>self.maxhealth:
            self.health=self.maxhealth
    def shoot(self):
        if self.shoot_timer>self.shoot_cooldown:
            self.shoot_timer=0
            proj=Projectile(self,self.vx,self.vy,GameConfig.PROJ_SIZE,self.projspeed,self.window)
            self.projs.append(proj)
            

    def stepLeft(self):
        self.rect.x-=self.speed

    def stepRight(self):
        self.rect.x+=self.speed

    def add_effect(self,_effect):
        effect=_effect
        effect.setPlayer(self)
        self.effects.append(effect)

    def update_projs(self):
        for proj in self.projs:
            proj.update()
            if proj.isdead:
                self.projs.remove(proj)

    def update_effects(self):
        for effect in self.effects:
            if effect.isdead:
                self.effects.remove(effect)
            effect.update()

    def update(self,bonuses,ennemies):
        self.ennemies=ennemies
        self.bonuses=bonuses
        self.update_projs()
        self.update_collisions(ennemies,bonuses)
        self.update_effects()
        self.shoot_timer+=1
        self.draw()
        self.update_spec(ennemies)
        

    def update_spec(self,ennemies):
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[self.kleft]:
            self.stepLeft()
        if keys[self.kright]:
            self.stepRight()
        if keys[self.kshoot]:
            self.shoot()


    def update_collisions(self,ennemies,bonuses):
            for proj in self.projs:
                for ennemy in ennemies:
                    if ennemy.rect.colliderect(proj.rect):
                        ennemy.attack(GameConfig.proj_damage)
                        self.projs.remove(proj)
                for bonus in bonuses:
                    if bonus.rect.colliderect(proj.rect):
                        self.add_effect(bonus.effect)
                        bonus.kill()

    def draw(self):
        healthtexture=self.texture
        healthwidth=round(GameConfig.PLAYER_W*self.health/self.maxhealth)
        pygame.draw.rect(healthtexture,self.color,(0,0,healthwidth,GameConfig.PLAYER_H))
        pygame.draw.rect(healthtexture,(80,80,80),(healthwidth,0,GameConfig.PLAYER_W-healthwidth,GameConfig.PLAYER_H))
        #pygame.draw.rect(healthtexture,self.color,(0,0,32,GameConfig.PLAYER_H))
        self.window.blit(healthtexture,(self.rect.x,self.rect.y))