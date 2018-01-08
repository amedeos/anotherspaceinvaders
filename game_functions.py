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
    elif event.key == pygame.K_s:
        ai_settings.bullet_width = ai_settings.bullet_width * 10
    elif event.key == pygame.K_a:
        ai_settings.bullet_width = ai_settings.bullet_width / 10

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

def update_bullets(ai_settings,  screen,  ship,  invaders,  bullets):
    """Update position of bullets and delete the old"""
    bullets.update()
    
    # remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # check for shot
    check_bullet_invader_collisions(ai_settings=ai_settings,  screen=screen,  ship=ship,  invaders=invaders,  bullets=bullets)

def check_bullet_invader_collisions(ai_settings,  screen,  ship,  invaders,  bullets):
    """check if bullet shot the invader"""
    collisions = pygame.sprite.groupcollide(bullets,  invaders,  True,  True)
    if len(invaders) == 0:
        bullets.empty()
        create_fleet(ai_settings=ai_settings,  screen=screen,  ship=ship,  invaders=invaders)

def fire_bullet(ai_settings,  screen,  ship,  bullets):
    """Fire a bullet"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings=ai_settings,  screen=screen,  ship=ship)
        bullets.add(new_bullet)

def get_number_invaders_x(ai_settings,  invader_width):
    """Calculate the number of invaders in a row"""
    available_space_x = ai_settings.screen_width - 2 * invader_width
    number_invaders_x = int( available_space_x / ( ai_settings.invader_width_factor * invader_width ) )
    return number_invaders_x

def create_invader(ai_settings,  screen,  invaders,  invader_number,  row_number):
    """Create an invader"""
    invader = Invader(ai_settings=ai_settings,  screen=screen)
    invader_width = invader.rect.width
    invader.x = invader_width + 2 * invader_width * invader_number
    invader.rect.x = invader.x
    invader.rect.y = invader.rect.height + 2 * invader.rect.height * row_number
    invaders.add(invader)

def create_fleet(ai_settings,  screen,  ship,  invaders):
    """Create a fleet of invaders"""
    invader = Invader(ai_settings,  screen)
    number_invaders_x = get_number_invaders_x(ai_settings,  invader.rect.width)
    number_rows = get_number_rows(ai_settings=ai_settings,  ship_height=ship.rect.height,  invader_height=invader.rect.height)
    
    for row_number in range(number_rows):
        for invader_number in range(number_invaders_x):
            create_invader(ai_settings=ai_settings,  screen=screen,  invaders=invaders,  invader_number=invader_number,  row_number=row_number)

def get_number_rows(ai_settings,  ship_height,  invader_height):
    """Calculate the number of rows of invaders"""
    available_space_y = (ai_settings.screen_height - (ai_settings.invader_height_factor * invader_height) - ship_height )
    number_rows = int( available_space_y / (2 * invader_height) )
    return number_rows

def update_invaders(ai_settings,  ship,  invaders):
    """Update the positions of all invaders"""
    check_fleet_edges(ai_settings=ai_settings,  invaders=invaders)
    invaders.update()
    
    # check for collisions with the ship
    if pygame.sprite.spritecollideany(ship,  invaders):
        print("Invaders hit the ship. You lose!")

def check_fleet_edges(ai_settings,  invaders):
    """check all invaders if there are on the edge"""
    for invader in invaders.sprites():
        if invader.check_edges():
            change_fleet_direction(ai_settings=ai_settings,  invaders=invaders)
            break

def change_fleet_direction(ai_settings,  invaders):
    """Drop the fleet and change direction"""
    for invader in invaders.sprites():
        invader.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
