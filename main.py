import pygame
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
        game_state.kb_input()

        

        game_state.draw(window)
        pygame.time.delay(20)
        pygame.display.update()


def main():   
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("Projet M3202")
    game_loop(window)

    pygame.quit()
    quit()

main() 