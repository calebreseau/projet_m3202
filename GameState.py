from Team import *
from Player import *
from bot import *
from Zone_neutre import *
from bot import *
from game_config import *

class GameState:   ## ajouter les differents ecrans possibles
    
    def init_players(self):
        for player in GameConfig.players:
            if player[0]==GameConfig.tpHuman:
                newplayer=Player(self.window,player[1],player[2],player[3])
                if player[4]==GameConfig.TeamUp:
                    self.teamup.add_player(newplayer)
                else:
                    self.teamdown.add_player(newplayer)
            if player[0]==GameConfig.tpAI:
                newplayer=Bot(self.window)
                if player[1]==GameConfig.TeamUp:
                    self.teamup.add_player(newplayer)
                else:
                    self.teamdown.add_player(newplayer)


    def __init__(self,x1,x2, window):
        
        self.window=window
        self.teamup=Team(GameConfig.teamup_vy,GameConfig.teamup_color,GameConfig.teamup_yspawn,None)
        self.teamdown=Team(GameConfig.teamdown_vy,GameConfig.teamdown_color,GameConfig.teamdown_yspawn,self.teamup)


        self.init_players()
        #player=PlayerDown(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,window)
        #self.players.append(player)

        #player=Bot(0,0,0,window)
        #self.players.append(player)

        self.zone = Zone_neutre(GameConfig.zonex1,GameConfig.zoney1,GameConfig.zonex2,GameConfig.zoney2,(GameConfig.zonex2/10)*2,window)

    def draw_sprites(self,window):
        for player in self.players:
            window.blit(player.texture, (player.rect.x,player.rect.y))

    def get_ennemies(self,typeennemies):
        ennemies=[]
        for player in self.players:
            if isinstance(player,typeennemies):
                ennemies.append(player)
        return ennemies

    def update(self) :
        self.draw()
        self.zone.update()
        self.teamdown.update_players(self.teamup)
        self.teamup.update_players(self.teamdown)

        #for player in self.players:
        #    if isinstance(player,Bot):
        #        player.update(self.get_ennemies(PlayerDown))
        #    else:
        #        player.update()
        #self.update_collisions()
                
    def draw(self):
        background = pygame.Surface((800,600))
        pygame.draw.rect(background,(0,0,0),(0,0,GameConfig.WINDOW_W,GameConfig.WINDOW_H))
        self.window.blit(background,(0,0))
