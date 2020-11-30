from Player import *
from game_config import *

class Bot(Player):

    def __init__ (self,window) :
        super().__init__(window)
        self.vectorX = 0
        self.tick = 0

    def update_spec(self, ennemies) :
        self.ennemies = ennemies
        self.est_menace()
        self.move()

    def move_left(self) :
        self.vectorX = -self.speed
    def move_right(self) :
        self.vectorX = self.speed
    def stop(self) :
        self.vectorX = 0
    def move(self) :
        if self.vectorX>0:
            self.stepRight()
        if self.vectorX<0:
            self.stepLeft()
       
    def get_position_on_tick(self, pos, vector, tick) :
        return [pos[0] + vector[0] * tick, pos[1] + vector[1] * tick]

#    def get_bullet_relative_trajectory(self,bullet) :
#        trajectory_function_min = [bullet.speed, bullet.rect.x]
#        trajectory_function_max = [bullet.speed, bullet.rect.x+GameConfig.PROJ_SIZE]
#        return[trajectory_function_min, trajectory_function_max] - self.get_trajectory_function()
#
#    def get_bullets_relatives_trajectories(self,ennemy) :
#        incomming_bullets = []
#        for bullet in self.ennemy.projs :
#            incomming_bullets.append(self.get_bullet_relative_trajectory(bullet))

   # def bullet_dangeureuse(self,trajectoire_relative) :
   #     for tic in range(20) :
   #         relative_position_min = tic * trajectoire[0][0] + trajectoire[0][1]
   #         relative_position_max = tic * trajectoire[1][0] + trajectoire[1][1]
   # 
    def est_menace(self) :
        for ennemy in self.ennemies :
            for bullet in ennemy.projs :
                if(self.simulation(bullet)) :
                   print("WAAAAAARNIIIIG")
    
    def simulation(self,bullet) :
        self.positions_relatives = []
        for i in range(GameConfig.bot_ticks_de_reflexion) :
            position_bullet = self.get_position_on_tick([bullet.rect.x, bullet.rect.y], [bullet.VX,bullet.VY] * bullet.speed,i)
            position_self = self.get_position_on_tick([self.rect.x, self.rect.y], [self.vectorX,self.rect.y],i)
            self.positions_relatives.append((position_bullet[0] - position_self[0], position_bullet[1] - position_self[1]))
        
        for position in self.positions_relatives :
           if (position[1] < GameConfig.PLAYER_H) and (position[1]+GameConfig.PROJ_SIZE > 0):
              
               if(position[0] < GameConfig.PLAYER_W) and (position[0]+GameConfig.PROJ_SIZE > 0) :
                   return True
        return False


        
