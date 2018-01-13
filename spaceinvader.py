#!/usr/bin/python3
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
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
    
    # game statistics
    stats = GameStats(ai_settings=ai_settings)
    sb = Scoreboard(ai_settings=ai_settings,  screen=screen,  stats=stats)
    
    # make the guardian of the invaders
    ship = Ship(ai_settings=ai_settings,  screen=screen)
    
    # make the enemy
    invaders = Group()
    gf.create_fleet(ai_settings=ai_settings,  screen=screen, ship=ship,  invaders=invaders)
    
    #create a bullet group
    bullets = Group()
    
    play_button = Button(ai_settings,  screen,  "Play")
    
    while True:
        gf.check_events(ai_settings=ai_settings, screen=screen, stats=stats,  scoreboard=sb,
                            play_button=play_button, ship=ship, invaders=invaders,  bullets=bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings=ai_settings,  screen=screen, stats=stats, 
                    scoreboard=sb, ship=ship,  invaders=invaders,  bullets=bullets)
            gf.update_invaders(ai_settings=ai_settings, stats=stats, scoreboard=sb,
                    screen=screen, ship=ship, invaders=invaders,  bullets=bullets)
        
        gf.update_screen(ai_settings=ai_settings,  stats=stats, scoreboard=sb,  screen=screen,  
                    ship=ship, invaders=invaders,  bullets=bullets,  play_button=play_button)

run_game()
