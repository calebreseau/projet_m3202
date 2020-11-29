from PlayerUp import *
from game_config import *

class Bot(PlayerUp):

    def update(self,ennemies):
        ennemy=ennemies[0]
        if ennemy.rect.x>self.rect.x:
            self.stepRight()
        else:
            self.stepLeft()
        self.draw()