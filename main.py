import pygame
from GameState import *
from game_config import *
from Player import *
from Zone_neutre import *
from Bonus import *


def game_loop(window):   ## ici ajouter aussi en lien avec game config un ecran de menu et un ecran de choix des personnages
    quitting=False
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
    tx=0
    ty=0
    game_state=GameState(tx,ty,window)
    game_state.draw(window)
    pygame.display.update()
    pygame.time.delay(20)

def kb_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players[0].stepLeft()
            if event.key == pygame.K_RIGHT:
                players[0].stepRight()

def main():   
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("Projet M3202")
    game_loop(window)

    pygame.quit()
    quit()

main() 