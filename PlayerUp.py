from Player import *

class PlayerUp(Player):
    def init_specs(self):        
        self.rect=pygame.Rect(GameConfig.player_xspawn,GameConfig.playerup_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.color=GameConfig.playerup_color
        self.vy=GameConfig.playerup_vy
        