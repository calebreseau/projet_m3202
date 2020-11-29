from Player import *

class PlayerUp(Player):
    def init_specs(self):        
        self.rect=pygame.Rect(GameConfig.player_xspawn,GameConfig.playerup_yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.texture=pygame.Surface((GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        pygame.draw.rect(self.texture,GameConfig.playerup_color,(0,0,GameConfig.PLAYER_W,GameConfig.PLAYER_H))
        self.vy=GameConfig.playerup_vy
        