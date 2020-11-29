from Player import *
from Zone_neutre import *

class GameState:   ## ajouter les differents ecrans possibles
    
    def __init__(self,tx,ty, window):
        pos=300
        self.players=[]
        player=Player('red.png',tx,ty,pos,2,100)
        self.players.append(player)
        print(self.players.count)

        #zone = Zone_neutre(0,100,800,300,87,window)

    def draw_sprites(self,window):
        for player in self.players:
            print(str(player))
            window.blit(player.texture, (player.rect.x,player.rect.y))

    def draw(self,window):
        self.draw_sprites(window)
        #zone.update()
