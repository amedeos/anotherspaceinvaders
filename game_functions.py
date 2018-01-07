import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship,  bullets):
    """Respond to keydown event"""
    if event.key == pygame.K_RIGHT:
        # let's move to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # let's move to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings=ai_settings,  screen=screen,  ship=ship)
        bullets.add(new_bullet)

def check_keyup_events(event,  ship):
    """Respond to keyup events"""
    if event.key == pygame.K_RIGHT:
        # stop moving to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop moving to the left
        ship.moving_left = False

def check_events(ai_settings,  screen, ship,  bullets):
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event=event, ai_settings=ai_settings,  screen=screen, ship=ship,  bullets=bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,  ship)

def update_screen(ai_settings,  screen,  ship,  bullets):
    """
    Update images on the screen and flip to the new screen
    """
    screen.fill(ai_settings.bg_color)
    # redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    pygame.display.flip()
