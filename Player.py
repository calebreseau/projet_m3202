class Player:
    def __init___(texture,terrain,pos,speed,maxhealth):
        self.texture=texture
        self.pos=pos
        self.speed=speed
        self.maxhealth=maxhealth

    def stepLeft():
        self.pos.x-=1

    def stepRight():
        self.pos.x+=1