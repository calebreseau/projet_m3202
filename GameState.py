from Player import *
from Zone_neutre import *

class GameState:   ## ajouter les differents ecrans possibles
    
    def __init__(self,tx,ty, window):
        pos=300
        players=[]
        player=Player('red.png',tx,ty,pos,2,100)
        players.append(player)
        print(players.count)

        zone = Zone_neutre(0,100,800,300,87,window)

    def draw(self,window):
        draw_sprites()
        zone.update()

    def draw_sprites(self,window):
        for player in players:
            print(str(player))
            window.blit(player.texture, (player.pos.x,player.pos.y))