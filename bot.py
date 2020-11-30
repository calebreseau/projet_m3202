from Player import *
from game_config import *
from random import *

class Bot(Player):

    def __init__ (self,window) :
        super().__init__(window)
        self.vectorX = 0
        self.tick = 0
        self.en_danger = False
        self.vectorX_states=[-1,0,1]
    def update_spec(self, ennemies) :
        self.ennemies = ennemies
        self.en_danger = self.est_menace()
        if(self.en_danger) :
            self.fuir()
        self.moove()

    def moove_left(self) :
        self.vectorX = -self.speed
    def moove_right(self) :
        self.vectorX = self.speed
    def stop(self) :
        self.vectorX = 0
    def moove(self) :
        self.rect.x += self.vectorX
    def fuir(self) :
        if(self.vectorX<0) :
            self.moove_left()
        else :
            self.moove_right()
            
        
    def get_position_on_tic(self, pos, vector, tick) :
        #print([pos[0] + vector[0] * tick, pos[1] + vector[1] * tick])
        return [pos[0] + vector[0] * tick, pos[1] + vector[1] * tick]




    def tick_avant_collision(self, posA, vectorA, tailleA, posB, vectorB, tailleB) :

        positions_relatives = []

        for i in range(GameConfig.bot_ticks_de_reflexion) :
            
            position_A = self.get_position_on_tic(posA, vectorA , i)
            
            position_B = self.get_position_on_tic(posB, vectorB, i)
            
            positions_relatives.append([position_A[0] - position_B[0], position_A[1] - position_B[1]])
        for position in positions_relatives :
           if (position[1] < tailleB) and (position[1]+tailleA > 0):
               if(position[0] < tailleB) and (position[0]+tailleA > 0) :
                   return positions_relatives.index(position)
        return -1


    def simulation(self,bullet) :
        tick_before_collision = self.tick_avant_collision([bullet.rect.x, bullet.rect.y],[bullet.VX * bullet.speed,bullet.VY * bullet.speed],GameConfig.PROJ_SIZE,[self.rect.x, self.rect.y],[self.vectorX,0],GameConfig.PLAYER_H)
        print(tick_before_collision)
        if(tick_before_collision>0) :
            return True
        else :
            return False
            



    def est_menace(self) :

        for ennemy in self.ennemies :
            for bullet in ennemy.projs :
                if(self.simulation(bullet)) :
                    return True
        return False

        
