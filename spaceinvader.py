#!/usr/bin/python3
import sys
import pygame

def run_game():
    """
    Initialize the game creating a screen object.
    """
    pygame.init()
    screen = pygame.display.set_mode((1200,  800))
    pygame.display.set_caption("Amedeo version of Space Invaders")
    
    while True:
        # control if there are a quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()
