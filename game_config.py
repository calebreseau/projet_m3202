class GameConfig:
   ## doit aussi contenir toutes les positions de depart des 6 différents joueurs pottentiels.
   ## doit contenir les variables par default des reglages ( 1 perso contre 1 PC )
    WINDOW_W = 800
    WINDOW_H = 600

    zonex1 = 0
    zonex2 = WINDOW_W
    zoney1 = 150
    zoney2 = 300

    PLAYER_W = 64
    PLAYER_H = 64
    PROJ_SIZE=16
    proj_lifetime=100
    player_vx=0
    player_vy=1
    player_projspeed=5
    player_maxhealth=100
    playerspeed = 5

    shoot_cooldown=20

    player_xspawn=300
    
    playerup_color=(0,0,255)
    playerup_vy=1
    playerup_yspawn=zoney1-PLAYER_H
    
    playerdown_color=(255,0,0)
    playerdown_vy=-1
    playerdown_yspawn=zoney1+zoney2

    bonus_size = 46
    bonus_spawn_X = WINDOW_W + bonus_size
    bonus_spawn_ymin = zoney1 + bonus_size
    bonus_spawn_ymax = zoney2 - bonus_size



     ### penser a charger ici l'integraliter des images une fois que pygame est lancé