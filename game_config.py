class GameConfig:
   ## doit aussi contenir toutes les positions de depart des 6 différents joueurs pottentiels.
   ## doit contenir les variables par default des reglages ( 1 perso contre 1 PC )
    WINDOW_W = 800
    WINDOW_H = 600
    PLAYER_W = 32
    PLAYER_H = 32
    playerspeed = 5
    zonex1 = 0
    zonex2 = WINDOW_W
    zoney1 = 150
    zoney2 = 300

    player_yspawn = zoney1 + zoney2
    ennemy_yspawn = zoney1-PLAYER_H

    bonus_size = 46
    bonus_spawn_X = WINDOW_W + bonus_size
    bonus_spawn_ymin = zoney1 + bonus_size
    bonus_spawn_ymax = zoney2 - bonus_size



     ### penser a charger ici l'integraliter des images une fois que pygame est lancé