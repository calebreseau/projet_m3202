class GameConfig:
   ## doit aussi contenir toutes les positions de depart des 6 différents joueurs pottentiels.
   ## doit contenir les variables par default des reglages ( 1 perso contre 1 PC )
    WINDOW_W = 800
    WINDOW_H = 600
    PLAYER_W = 32
    PLAYER_H = 32
    playerspeed = 20
    zonex1 = 0
    zonex2 = WINDOW_W
    zoney1 = 150
    zoney2 = 300

    player_yspawn = zoney1 + zoney2
    ennemy_yspawn = zoney1-PLAYER_H



     ### penser a charger ici l'integraliter des images une fois que pygame est lancé