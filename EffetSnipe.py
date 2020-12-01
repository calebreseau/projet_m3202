from Effet import *

class EffetSnipe(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(255,0,255)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))

    def apply_effect(self):
        self.player.projspeed*=2
    
    def restore_player(self):
        self.player.projspeed/=2
