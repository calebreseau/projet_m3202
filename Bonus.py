from random import *
import pygame
from game_config import *
from Player import *
from EffetHeal import *
from EffetReverse import *
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
		Y = normalvariate((ymax+ymin)/2,(ymin-ymax)/6)
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
		self.window.blit(self.effect.image,(self.rect.x,self.rect.y))
