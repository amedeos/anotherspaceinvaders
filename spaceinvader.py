#!/usr/bin/python3
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

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
    
    # make the guardian of the invaders
    ship = Ship(screen=screen,  ship_image=ai_settings.ship_image)
    
    while True:
        gf.check_events()
        gf.update_screen(ai_settings=ai_settings,  screen=screen,  ship=ship)

run_game()
