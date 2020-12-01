from Player import *
from game_config import *
import time
import inspect

class Effet:
    
    def apply_effect(self):
        pass

    def restore_player(self):
        pass

    def kill(self):
        self.restore_player()
        self.isdead=True

    def __init__(self):
        self.isApplied=False
        self.isdead=False
        self.player=None
        self.lifepercentage=1
        self.cooldown=GameConfig.effect_defcooldown

    def setPlayer(self,player):
        self.player=player
        self.timer=0

    def update(self):
        if self.isdead==True: 
            return
        if self.player != None:
            if self.isApplied==False:
                self.apply_effect()
                self.isApplied=True
                self.timer=time.time() 
            self.lifepercentage=round(1000*(time.time()-self.timer))/self.cooldown
            if round(1000*(time.time()-self.timer))>self.cooldown:
                self.kill()

        
