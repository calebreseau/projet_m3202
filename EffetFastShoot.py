from Effet import *

class EffetFastShoot(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(0,255,255)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown=5000

    def apply_effect(self):
        self.player.shoot_cooldown/=2
    
    def restore_player(self):
        self.player.shoot_cooldown*=2
