import pygame

class GameConfig:
   ## doit aussi contenir toutes les positions de depart des 6 différents joueurs pottentiels.
   ## doit contenir les variables par default des reglages ( 1 perso contre 1 PC )
    GameName='Projet M3202'
   
    WINDOW_W = 1200
    WINDOW_H = 600


    tpNone = 0
    tpHuman = 1
    tpAI = 2

    TeamDown = 0
    TeamUp = 1  
    
    players_bot=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpAI,TeamUp]] #joueur vs IA
    players_humans=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpHuman,pygame.K_q,pygame.K_d,pygame.K_z,TeamUp]] #joueur vs joueur
    players_hvb=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpHuman,pygame.K_q,pygame.K_d,pygame.K_z,TeamDown],[tpAI,TeamUp],[tpAI,TeamUp]]
    players_hbvhb=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpHuman,pygame.K_q,pygame.K_d,pygame.K_z,TeamUp],[tpAI,TeamUp],[tpAI,TeamDown]]
    players_3bot=[[tpHuman,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,TeamDown],[tpAI,TeamUp],[tpAI,TeamUp],[tpAI,TeamDown]]
    players_fullbots4=[[tpAI,TeamUp],[tpAI,TeamUp],[tpAI,TeamDown],[tpAI,TeamDown]]
    players_fullbots2=[[tpAI,TeamUp],[tpAI,TeamDown]]
    playerstemplates=[players_bot,players_humans,players_hvb,players_hbvhb,players_3bot,players_fullbots2,players_fullbots4]

    players=[]
    zonex1 = 0
    zonex2 = WINDOW_W*2
    zoney1 = 150
    zoney2 = 300

    PLAYER_W = 64
    PLAYER_H = 64
    PROJ_SIZE=16
    proj_lifetime=50
    proj_damage=20
    player_vx=0.0
    player_vy=1.0
    player_projspeed=10.0
    player_maxhealth=100
    playerspeed = 4.0

    tdrs=[1,2,3]
 
    bot_ticks_de_reflexion = 2

    shoot_cooldown=20

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
    bonus_times = [7,5,3]
    bonus_average_time_between_bonus = 6

    effecttypes=['EffetHeal','EffetSnipe','EffetFastShoot','EffetSlow','EffetStunned','EffetFrenesie']
   
    hud_el_size=32

    delay_between_tick = 20

     ### penser a charger ici l'integraliter des images une fois que pygame est lancé