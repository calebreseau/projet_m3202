from random import *
import pygame
from game_config import *
from Player import *
from EffetHeal import *
from EffetSlow import *
from EffetSnipe import *
from EffetFastShoot import *
from EffetStunned import *
from EffetFrenesie import *
import sys

class Bonus :

	def create_effect(self):
		name=self.effectname
		mod=sys.modules[name]
		_class=getattr(mod,name)
		inst=_class()
		return inst

	def __init__ (self,x,ymin,ymax,typeMax,Zone_neutre,Window) :
		self.isDead=False
		effID=randint(0,typeMax)
		self.effectname=GameConfig.effecttypes[effID]
		self.effect = self.create_effect()
		self.image=self.effect.image
		Y = normalvariate((ymax+ymin)/2+GameConfig.bonus_size,(ymin-ymax)/6)
		self.rect=pygame.Rect(x,Y,GameConfig.bonus_size,GameConfig.bonus_size)

		self.zone_neutre = Zone_neutre
		self.window = Window

	def kill(self):
		self.isDead=True

	def update(self) :
		self.speed = self.zone_neutre.speed
		self.move()
		
	def move(self) :
		self.rect.x-=self.speed

	def draw(self) : 
		textsurface=GameConfig.bonusfont.render(self.effectname.replace('Effet',''),False,(0,0,0))
		self.window.blit(self.effect.image,(self.rect.x,self.rect.y))
		self.window.blit(textsurface,(self.rect.x,int(self.rect.y+GameConfig.bonus_size/3)))
