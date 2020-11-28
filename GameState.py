from Player import *

class GameState:
    
    def __init__(self,tx,ty):
        pos=300
        players=[]
        player=Player('red.png',tx,ty,pos,2,100)
        players.add(player)
        print(players.count)

    def draw(self,window):
        draw_sprites()

    def draw_sprites(self,window):
        for player in players:
            print(str(player))
            window.blit(player.texture, (player.pos.x,player.pos.y))