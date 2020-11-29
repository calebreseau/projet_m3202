from Player import *

class PlayerDown(Player):
    def init_specs(self):       
        self.rect=pygame.Rect(GameConfig.player_xspawn,GameConfig.playerdown_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.color=GameConfig.playerdown_color
        self.vy=GameConfig.playerdown_vy
