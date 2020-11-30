from random import *
from game_config import *
from Bonus import *
import pygame
import time
from game_config import *

class Zone_neutre :
	
	def __init__ (self,X1,Y1,x2,y2,img_step,Window) :
		self.x1 = X1
		self.y1 = Y1
		self.imageX = X1
		self.image_step = img_step
		self.speed = 1
		#image = pygame.image.load('img/tapis_roulant.png')
		self.image=pygame.Surface((x2,y2))
		#pygame.draw.rect(self.image,(75,90,80),(0,0,self.x2,self.y2))
		color=(30,30,30)
		for i in range(round(x2/10)):
			pygame.draw.rect(self.image,color,(round(i*(x2/10)),0,round(x2/10),x2))
			if color==(75,75,75):
				color=(30,30,30)
			else:
				color=(75,75,75)
		
		self.window = Window

		self.all_bonus = []
		self.time_since_last_bonus = time.time()
		self.average_time_between_bonus = GameConfig.bonus_average_time_between_bonus
		self.time_before_next_bonus = expovariate(1 / self.average_time_between_bonus)
		
	def update(self) :
		self.scroll()
		self.update_bonus()

		if(time.time() - self.time_since_last_bonus > self.time_before_next_bonus) :
			self.generate_bonus()
			self.time_since_last_bonus = time.time()
			self.time_before_next_bonus = expovariate(1 / self.average_time_between_bonus)

		self.draw()


	def generate_bonus(self) :
		      ##a modifier, genere les bonus 0.17 par tic
		bonus = Bonus(GameConfig.bonus_spawn_X, GameConfig.bonus_spawn_ymin, GameConfig.bonus_spawn_ymax, len(GameConfig.effecttypes)-1, self, self.window)
		self.all_bonus.append(bonus)

	def update_bonus(self) :
		for i in self.all_bonus :
			i.update()
			if i.rect.x < self.x1 :
				i.kill()
			if i.isDead:
				self.all_bonus.remove(i)
				
	def scroll(self) :
		self.imageX-=self.speed
		if self.x1 > self.imageX + 2* self.image_step :
			self.imageX+=self.image_step
	def draw(self) :
		self.window.blit(self.image,(self.imageX,self.y1))
		for i in self.all_bonus :
			i.draw()
