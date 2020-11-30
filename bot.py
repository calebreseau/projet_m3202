from Player import *
from game_config import *

class Bot(Player):

    def update(self,ennemies):
        ennemy=ennemies[0]
        if ennemy.rect.x>self.rect.x:
            self.stepRight()
        else:
            self.stepLeft()
        self.draw()
class Bot(Player):

    def __init__ (self,window) :
        super().__init__(window)
        self.est_en_joue = False
        self.est_menace = False

    def update(self, ennemies) :





    