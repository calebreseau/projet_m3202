from Effet import *

class EffetSlow(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        pygame.draw.rect(self.image,(255,255,0),(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown=5000

    def apply_effect(self):
        for player in self.player.ennemies:
            player.speed=player.speed/2
    
    def restore_player(self):
        for player in self.player.ennemies:
            player.speed=player.speed*2
