import pygame

class GameConfig:
   ## doit aussi contenir toutes les positions de depart des 6 différents joueurs pottentiels.
   ## doit contenir les variables par default des reglages ( 1 perso contre 1 PC )
    WINDOW_W = 800
    WINDOW_H = 600


    tpHuman = 0
    tpAI = 1

    TeamDown = 0
    TeamUp = 1

    players=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpAI,TeamUp]] #joueur vs IA
    #players=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpHuman,pygame.K_q,pygame.K_d,pygame.K_z,TeamUp]] #joueur vs joueur
    zonex1 = 0
    zonex2 = WINDOW_W*2
    zoney1 = 150
    zoney2 = 300

    PLAYER_W = 64
    PLAYER_H = 64
    PROJ_SIZE=16
    proj_lifetime=30
    proj_damage=10
    player_vx=0
    player_vy=1
    player_projspeed=20
    player_maxhealth=100
    playerspeed = 5.0

    bot_ticks_de_reflexion = 15

    shoot_cooldown=75

    player_xspawn=300
    
    teamup_color=(0,0,255)
    teamup_vy=1
    teamup_yspawn=zoney1-PLAYER_H*2
    
    teamdown_color=(255,0,0)
    teamdown_vy=-1
    teamdown_yspawn=zoney1+zoney2+PLAYER_H

    bonus_size = 46
    bonus_spawn_X = WINDOW_W + bonus_size
    bonus_spawn_ymin = zoney1 + bonus_size
    bonus_spawn_ymax = zoney2 - bonus_size
    bonus_average_time_between_bonus = 6

    effecttypes=['EffetHeal','EffetReverse','EffetSlow']

    hud_el_size=32

     ### penser a charger ici l'integraliter des images une fois que pygame est lancé