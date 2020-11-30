from Effet import *
from Player import *
import pygame

class EffetHeal(Effet):

    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((GameConfig.bonus_size,GameConfig.bonus_size))
        pygame.draw.rect(self.image,(255,0,0),(0,0,GameConfig.bonus_size,GameConfig.bonus_size))
        self.cooldown=500

    def apply_effect(self):
        self.defplayer.heal(20)

