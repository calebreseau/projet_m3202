from game_config import *
from Player import *

class Team:

    def setennemyteam(self,ennemyteam):
        if ennemyteam!=None:
            self.ennemyteam=ennemyteam
            ennemyteam.ennemyteam=self
    
    def __init__(self,vy,color,yspawn,ennemyteam):
        self.players=[]
        self.setennemyteam(ennemyteam)
        self.vy=vy
        self.color=color
        self.yspawn=yspawn

    def add_player(self,player):
        player.rect=pygame.Rect(GameConfig.player_xspawn,self.yspawn,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        player.color=self.color
        player.vy=self.vy
        self.players.append(player)

    def update_players(self,ennemyteam):
        for player in self.players:
            if player.update==player.update_human:
                player.update()
            else:
                player.update(ennemyteam.players)
            player.update_collisions(ennemyteam.players)


