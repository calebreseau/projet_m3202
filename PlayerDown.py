from Player import *

class PlayerDown(Player):
    def init_specs(self):       
        self.rect=pygame.Rect(GameConfig.player_xspawn,GameConfig.playerdown_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.texture=pygame.Surface((GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        pygame.draw.rect(self.texture,GameConfig.playerdown_color,(0,0,GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        self.vy=GameConfig.playerdown_vy
