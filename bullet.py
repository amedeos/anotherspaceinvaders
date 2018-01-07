import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets"""
    
    def __init__(self,  ai_settings,  screen,  ship):
        """Create a bullet at the ship position"""
        super().__init__()
        self.screen = screen
        
        # create a bullet rectangle
        self.rect = pygame.Rect(0,  0,  ai_settings.bullet_width,  ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # create a float var with the y position
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """Update the bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen,  self.color,  self.rect)
