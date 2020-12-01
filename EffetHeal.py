from Effet import *
from Player import *
import pygame

class EffetHeal(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        self.color=(255,0,0)
        pygame.draw.rect(self.image,self.color,(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown/=20

    def apply_effect(self):
        self.player.heal(20)

    def restore_player(self):
        pass

