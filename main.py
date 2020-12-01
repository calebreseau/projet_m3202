import pygame
import pygame_menu
from GameState import *
from game_config import *
from Player import *
from Zone_neutre import *
from Bonus import *


def game_loop(window):   ## ici ajouter aussi en lien avec game config un ecran de menu et un ecran de choix des personnages
    quitting=False

    tx=0
    ty=0
    game_state=GameState(tx,ty,window)
    time_before_update_delay_time = GameConfig.bot_ticks_de_reflexion * 50
    GameConfig.delay_between_tick = 40 - GameConfig.bot_ticks_de_reflexion * 10
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        updresult=game_state.update()
        if updresult!=3:
            endmenu(updresult)
            quitting=True
        if(time_before_update_delay_time < 0) and (GameConfig.delay_between_tick>(6 - GameConfig.bot_ticks_de_reflexion)*2) :   # acceleration du jeu
            print(GameConfig.delay_between_tick)
            GameConfig.delay_between_tick -= 1
            time_before_update_delay_time = GameConfig.bot_ticks_de_reflexion * 100     # en fonction de la difficulté
        else :
            time_before_update_delay_time-=1
        pygame.time.delay(GameConfig.delay_between_tick)
        pygame.display.update()


def endmenu(winnerteam):
    menu = pygame_menu.Menu(GameConfig.WINDOW_H, GameConfig.WINDOW_W, 'Fin de partie!', theme=pygame_menu.themes.THEME_DARK)
    if winnerteam==GameConfig.TeamUp:
        winner='du bas'
    elif winnerteam==GameConfig.TeamDown:
        winner='du haut'
    menu.add_label('Victoire de l\'équipe '+winner+'!')
    #self.playeroptions=self.menu.add_selector('Type :', [('Pas en jeu', GameConfig.tpNone), ('Humain',GameConfig.tpHuman), ('IA', GameConfig.tpAI)], onchange=setplayertype)
    menu.add_button('Rejouer', start_game)
    menu.add_button('Aller au menu principal', main)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(window)

    
def setgametype(value, args):
    pygame.display.set_caption(GameConfig.GameName+': '+str(value[0]))
    GameConfig.players=GameConfig.playerstemplates[value[1]]
    

def setiadiff(value,args):
    GameConfig.bot_ticks_de_reflexion=GameConfig.tdrs[value[1]]

def setbonusfreq(value,args):
    GameConfig.bonus_average_time_between_bonus=GameConfig.bonus_times[value[1]]

def start_game():
    GameConfig.delay_between_tick = 30 - GameConfig.bot_ticks_de_reflexion*5
    game_loop(window)

def main():   
    pygame.display.set_caption("Projet M3202")
    setgametype(('Joueur (Gauche,Droite,Haut) contre IA',0),None)
    setiadiff((None,0),None)
    setbonusfreq
    menu = pygame_menu.Menu(GameConfig.WINDOW_H, GameConfig.WINDOW_W, 'Projet M3202: Accueil', theme=pygame_menu.themes.THEME_DARK)
    menu.add_selector('Partie :', 
        [('Joueur (Gauche,Droite,Haut) contre IA',0),
        ('Joueur (Gauche,Droite,Haut) contre Joueur(Q,D,Z)',1),
        ('2 Humains (G,D,H) et (Q,D,Z) contre 2 IA',2),
        ('2 Equipes de 1 Humain et 1 IA',3),
        ('2v2 en solo (G,D,H)',4),
        ('IA contre IA (1c1)',5),
        ('IA contre IA (2c2)',6)
        ], onchange=setgametype)
    menu.add_selector('Difficulté des IA :', 
        [('Facile',0),('Normal',1),('Difficile',2)], onchange=setiadiff)
    menu.add_selector('Fréquence d\'apparition des bonus :', 
        [('Petite',0),('Normale',1),('Elevée',2)], onchange=setbonusfreq)
    menu.add_button('Jouer', start_game)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(window)

    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
main() 