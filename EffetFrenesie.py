from Effet import *
import random

class EffetFrenesie(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(0,128,128)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))

    def apply_effect(self):
        self.player.shoot_cooldown/=2

    def restore_player(self):
        self.player.vx=GameConfig.player_vx
        self.player.shoot_cooldown*=2

    def update(self):
        super().update()
        if self.isdead==False:
            self.player.vx=random.random()-0.5
