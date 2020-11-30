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
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        
        game_state.update()
        pygame.time.delay(20)
        pygame.display.update()



def setgametype(value, args):
    print(str(value))
    GameConfig.players=GameConfig.playerstemplates[value[1]]

def start_game():
    game_loop(window)
def main():   
    pygame.display.set_caption("Projet M3202")

    menu = pygame_menu.Menu(GameConfig.WINDOW_H, GameConfig.WINDOW_W, 'Projet M3202', theme=pygame_menu.themes.THEME_DARK)
    menu.add_selector('Partie :', 
        [('Joueur (Gauche,Droite,Haut) contre IA',0),
        ('Joueur (Gauche,Droite,Haut) contre Joueur(Q,D,Z)',1)], onchange=setgametype)
    #self.playeroptions=self.menu.add_selector('Type :', [('Pas en jeu', GameConfig.tpNone), ('Humain',GameConfig.tpHuman), ('IA', GameConfig.tpAI)], onchange=setplayertype)
    menu.add_button('Play', start_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(window)

    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
main() 