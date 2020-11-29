from random import *
from game_config import *
from Bonus import *
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
		pygame.draw.rect(self.image,(75,90,80),(0,0,self.x2,self.y2))
		self.window = Window

		self.all_bonus = []

	def update(self) :
		self.scroll()
		self.update_bonus()
		self.generate_bonus()
		self.draw()


	def generate_bonus(self) :
		if(randint(0,100)>98) :      ##a modifier, genere les bonus 0.17 par tic
			bonus = Bonus(GameConfig.bonus_spawn_X, GameConfig.bonus_spawn_ymin, GameConfig.bonus_spawn_ymax, 3, self, self.window)
			self.all_bonus.append(bonus)

	def update_bonus(self) :
		for i in self.all_bonus :
			i.update()
			if i.X < self.x1 :
				self.all_bonus.remove(i)
	def scroll(self) :
		self.imageX-=self.speed
		if self.x1 > self.imageX + 2* self.image_step :
			self.imageX+=self.image_step
	def draw(self) :
		self.window.blit(self.image,(self.imageX,self.y1))
		for i in self.all_bonus :
			i.draw()
