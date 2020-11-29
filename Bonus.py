class Bonus :
	images = ["image1.png","etc"]
	def __init__ (self,x,ymin,ymax,typeMax,Zone_neutre,Window) :
		X = x
		Y = randint(ymin,ymax)
		type = randint(0,typeMax)
		zone_neutre = Zone_neutre
		window = Window
		image = pygame.image.load("image" + type + ".png")      # a modifier en fonction des images
	def update() :
		speed = zone_neutre.speed
		moove(speed)
		draw()
	def moove() :
		X-=speed
	def draw() : 
		window.blit(image,(X,Y))
