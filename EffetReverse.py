from Effet import *

class EffetReverse(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        pygame.draw.rect(self.image,(0,255,255),(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown=5000

    def apply_effect(self):
        tmp=self.player.kleft
        self.player.kleft=self.player.kright
        self.player.kright=tmp