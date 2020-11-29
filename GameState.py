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
            if isinstance(player,typeennemies):
                ennemies.append(player)
        return ennemies

    def update_collisions(self):
        for player in self.players:
            if isinstance(player,PlayerDown):
                ennemies=self.get_ennemies(PlayerUp)
            if isinstance(player,PlayerUp):
                ennemies=self.get_ennemies(PlayerDown)
            for proj in player.projs:
                #print(str(proj.rect.x)+','+str(proj.rect.y))
                for ennemy in ennemies:
                    print(str(ennemy.rect.x)+','+str(ennemy.rect.y))
                    if ennemy.rect.colliderect(proj.rect):
                        print('collide')
                        ennemy.attack(GameConfig.proj_damage)
                        print(str(ennemy.health))
                        player.projs.remove(proj)

    def update(self) :
        self.draw()
        self.zone.update()
        for player in self.players:
            if isinstance(player,Bot):
                player.update(self.get_ennemies(PlayerDown))
            else:
                player.update()
        self.update_collisions()
                
    def draw(self):
        background = pygame.Surface((800,600))
        pygame.draw.rect(background,(0,0,0),(0,0,GameConfig.WINDOW_W,GameConfig.WINDOW_H))
        self.window.blit(background,(0,0))
