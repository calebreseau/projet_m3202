from random import *
import pygame
from game_config import *

class Bonus :
	def __init__ (self,x,ymin,ymax,typeMax,Zone_neutre,Window) :
		print('new bonus')
		self.X = x
		self.Y = normalvariate(300,60)
		self.type = randint(0,typeMax)
		self.zone_neutre = Zone_neutre
		self.window = Window
		
		self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
		pygame.draw.rect(self.image,(0,233,0),(0,0,GameConfig.bonus_size,GameConfig.bonus_size))

	def update(self) :
		self.speed = self.zone_neutre.speed
		self.move()
		
	def move(self) :
		self.X-=self.speed
	def draw(self) : 
		self.window.blit(self.image,(self.X,self.Y))
