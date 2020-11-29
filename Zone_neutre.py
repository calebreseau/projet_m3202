from random import *
from game_config import *
import pygame
class Zone_neutre :
	
	def __init__ (self,X1,Y1,X2,Y2,img_step,Window) :
		x1 = X1
		y1 = Y1
		x2 = X2
		y2 = Y2
		imageX = X1
		image_step = img_step
		speed = 1
		#image = pygame.image.load('img/tapis_roulant.png')
		image=pygame.Surface((x2,y2))
		pygame.draw.rect(image,(75,90,80),(x1,y1,x2,y2))
		window = Window

		all_bonus = []

	def update(self) :
		scroll()
		update_bonus(speed)
		generate_bonus()
		draw()


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
		window.blit(image,(imageX,y1))
