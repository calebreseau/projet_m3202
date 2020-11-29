from random import *
from game_config import *
import pygame
class Zone_neutre :
	
	def __init__ (self,X1,Y1,X2,Y2,img_step,Window) :
		self.x1 = X1
		self.y1 = Y1
		self.x2 = X2
		self.y2 = Y2
		self.imageX = X1
		self.image_step = img_step
		self.speed = 1
		#image = pygame.image.load('img/tapis_roulant.png')
		self.image=pygame.Surface((self.x2,self.y2))
		pygame.draw.rect(self.image,(75,90,80),(self.x1,self.y1,self.x2,self.y2))
		self.window = Window

		self.all_bonus = []

	def update(self) :
		scroll()
		update_bonus(speed)
		generate_bonus()


	def generate_bonus(self) :
		if(randint(0,100)>93) :      ##a modifier, genere les bonus 0.17 par tic
			all_bonus.add(Bonus(X2+20, y1, y2, 3, self, window))

	def update_bonus(speed ) :
		for i in all_bonus :
			all_bonus[i].update()
			if i.X < x1 :
				all_bonus[i] = null
	def scroll(self) :
		imageX-=speed
		if x1 > imageX + 2*image_step :
			imageX+=image_step
	def draw(self) :
		self.window.blit(self.image,(self.imageX,self.y1))
