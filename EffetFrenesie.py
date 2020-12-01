from EffetFastShoot import *
from EffetStunned import *

class EffetFrenesie(EffetFastShoot):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(0,128,128)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))

    def apply_effect(self):
        super().apply_effect()
        effect=EffetStunned()
        effect.setPlayer(self.player.ennemies[0])
        self.player.ennemies[0].effects.append(effect)