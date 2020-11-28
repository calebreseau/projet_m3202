import pygame
from game_config import *

def game_loop():
    quitting=False
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

def main():
    pygame.init()
    window = pygame.display.set_mode((game_config.WINDOW_W,game_condig.WINDOW_H))
    pygame.display.set_caption("Projet M3202")
    game_loop()
    pygame.quit()
    quit()

main() 