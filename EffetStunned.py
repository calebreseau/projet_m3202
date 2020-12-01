from Effet import *
import random

class EffetStunned(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(128,255,128)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown=5000

    def apply_effect(self):
        pass
    
    def restore_player(self):
        for player in self.player.ennemies:
            player.vx=GameConfig.player_vx

    def update(self):
        super().update()
        for player in self.player.ennemies:
            if self.isdead==False:
                player.vx=random.random()-0.5

