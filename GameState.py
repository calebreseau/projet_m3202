from PlayerUp import *
from PlayerDown import *
from bot import *
from Zone_neutre import *
from bot import *
from game_config import *
class GameState:   ## ajouter les differents ecrans possibles
    
    def __init__(self,x1,x2, window):
        pos=300
        self.window=window
        self.players=[]
        player=PlayerDown(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,window)
        self.players.append(player)

        player=Bot(0,0,0,window)
        self.players.append(player)

        self.zone = Zone_neutre(GameConfig.zonex1,GameConfig.zoney1,GameConfig.zonex2,GameConfig.zoney2,87,window)

    def draw_sprites(self,window):
        for player in self.players:
            window.blit(player.texture, (player.rect.x,player.rect.y))

    def get_ennemies(self,typeennemies):
        ennemies=[]
        for player in self.players:
            if type(player) is typeennemies:
                ennemies.append(player)
        return ennemies

    def update(self) :
        self.draw()
        self.zone.update()
        for player in self.players:
            if isinstance(player,Bot):
                player.update(self.get_ennemies(PlayerDown))
            else:
                player.update()
                
    def draw(self):
        background = pygame.Surface((800,600))
        pygame.draw.rect(background,(0,0,0),(0,0,GameConfig.WINDOW_W,GameConfig.WINDOW_H))
        self.window.blit(background,(0,0))
