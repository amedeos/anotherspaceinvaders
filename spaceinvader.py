#!/usr/bin/python3
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from invader import Invader
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
    ship = Ship(ai_settings=ai_settings,  screen=screen)
    
    # make the enemy
    invaders = Group()
    gf.create_fleet(ai_settings=ai_settings,  screen=screen, ship=ship,  invaders=invaders)
    
    #create a bullet group
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship,  bullets=bullets)
        ship.update()
        gf.update_bullets(ai_settings=ai_settings,  screen=screen,  ship=ship,  invaders=invaders,  bullets=bullets)
        gf.update_invaders(ai_settings=ai_settings, ship=ship, invaders=invaders)
        gf.update_screen(ai_settings=ai_settings,  screen=screen,  ship=ship, invaders=invaders,  bullets=bullets)

run_game()
