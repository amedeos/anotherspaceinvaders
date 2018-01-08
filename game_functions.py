import sys
import pygame

from bullet import Bullet
from invader import Invader

def check_keydown_events(event, ai_settings, screen, ship,  bullets):
    """Respond to keydown event"""
    if event.key == pygame.K_RIGHT:
        # let's move to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # let's move to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings=ai_settings,  screen=screen,  ship=ship,  bullets=bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen(ai_settings,  screen,  ship, invaders, bullets):
    """
    Update images on the screen and flip to the new screen
    """
    screen.fill(ai_settings.bg_color)
    # redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    invaders.draw(screen)
    
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and delete the old"""
    bullets.update()
    
    # remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,  screen,  ship,  bullets):
    """Fire a bullet"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings=ai_settings,  screen=screen,  ship=ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,  screen,  invaders):
    """Create a fleet of invaders"""
    invader = Invader(ai_settings,  screen)
    invader_width = invader.rect.width
    available_space_x = ai_settings.screen_width - 2 * invader_width
    number_invaders_x = int( available_space_x / ( 2 * invader_width ) )
    
    for invader_number in range(number_invaders_x):
        invader = Invader(ai_settings,  screen)
        invader.x = invader_width +2 * invader_width * invader_number
        invader.rect.x = invader.x
        invaders.add(invader)
