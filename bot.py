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
        if(not self.en_danger) :
            if(randint(0,100 - GameConfig.bot_ticks_de_reflexion) == randint(0,100 - GameConfig.bot_ticks_de_reflexion) ) :
                self.fuir()   #deplacement aléatoire pour surprendre ladversaire en fonction de la difficulté de l'IA

        else :
            self.fuir()
        self.move()

        if(self.has_a_target_on_ennemy()) :
            self.shoot()


        if(self.has_a_target_on_a_bonus()) :
            if(randint(0,3) <= GameConfig.tdrs.index(GameConfig.bot_ticks_de_reflexion)) :

                self.shoot()




    def move_left(self) :
        self.vectorX = -self.speed
    def move_right(self) :
        self.vectorX = self.speed
    def stop(self) :
        self.vectorX = 0


    def move(self) :
        if(self.vectorX<0) :
            if(self.rect.x + self.vectorX>self.xlimitleft) :
                self.stepLeft()
            else :
                self.move_right()
            
        if(self.vectorX>0) :
            if(self.rect.x + self.vectorX + GameConfig.PLAYER_W<self.xlimitright) :
                self.stepRight()
            else :
                self.move_left()

        
        
    def fuir(self) :
        if(self.vectorX==0) :
            if(randint(0,1)==0) :

                self.move_left()
            else :
                self.move_right()
        else :
            if(self.vectorX>0) :
                if(randint(0,1)==0) :
                    self.move_left()
                else :
                    self.stop
            else :
                if(randint(0,1)==0) :
                    self.move_right()
                else :
                    self.stop
            
        
    def get_position_on_tic(self, pos, vector, tick) :
        return [pos[0] + vector[0] * tick, pos[1] + vector[1] * tick]




    def tick_avant_collision(self, posA, vectorA, tailleA, posB, vectorB, tailleB) :

        positions_relatives = []

        for i in range(70) :
            
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
        if(tick_before_collision>0) and(tick_before_collision< GameConfig.bot_ticks_de_reflexion) :
            return True
        else :
            return False
            



    def est_menace(self) :

        for ennemy in self.ennemies :
            for bullet in ennemy.projs :
                if(self.simulation(bullet)) :
                    return True
        return False




    def has_a_target_on_a_bonus(self) :
        for bonus in self.bonuses :
            tick_avant_impact = self.tick_avant_collision([self.rect.x+GameConfig.PLAYER_W/2-GameConfig.PROJ_SIZE/2, self.rect.y+GameConfig.PLAYER_W],[self.vx * self.projspeed,self.vy * self.projspeed],GameConfig.PROJ_SIZE,[bonus.rect.x, bonus.rect.y],[bonus.zone_neutre.speed*-1,0],GameConfig.bonus_size)
            if(tick_avant_impact>0) :
                return True
        return False


    def has_a_target_on_ennemy(self) :
        for ennemy in self.ennemies :



            tick_avant_impact = self.tick_avant_collision([self.rect.x+GameConfig.PLAYER_W/2-GameConfig.PROJ_SIZE/2, self.rect.y+GameConfig.PLAYER_W],[self.vx * self.projspeed,self.vy * self.projspeed],GameConfig.PROJ_SIZE,[ennemy.rect.x, ennemy.rect.y],[ennemy.directionX,0],GameConfig.PLAYER_W)
            if(tick_avant_impact>0) :
                return True
        return False

        
