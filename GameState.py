from Player import *
from Zone_neutre import *

import game_config
class GameState:   ## ajouter les differents ecrans possibles
    
    def __init__(self,tx,ty, window):
        pos=300
        self.players=[]
        player=Player('red.png',tx,ty,pos,GameConfig.playerspeed,100)
        self.players.append(player)
        print(self.players.count)

        zone = Zone_neutre(zonex1,zoney1,zonex2,zoney2,87,window)

    def draw_sprites(self,window):
        for player in self.players:
            window.blit(player.texture, (player.rect.x,player.rect.y))

    def kb_input(self):
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            self.players[0].stepLeft()
        if keys[pygame.K_RIGHT]:
            self.players[0].stepRight()
        #if event.key == pygame.K_LEFT:
        #    self.players[0].stepLeft()
        #if event.key == pygame.K_RIGHT:
        #    self.players[0].stepRight()
                
    def draw(self,window):
        background = pygame.Surface((800,600))
        ##pygame.display.update()
        self.draw_sprites(window)
        #zone.update()
