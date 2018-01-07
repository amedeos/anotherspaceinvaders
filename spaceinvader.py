#!/usr/bin/python3
import sys
import pygame

from settings import Settings

def run_game():
    """
    Initialize the game creating a screen object.
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                    (ai_settings.screen_width,  
                    ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    
    while True:
        # control if there are a quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # set the desired background color
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()

run_game()
