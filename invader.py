import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
    """
    A class to represent a single invader.
    """
    
    def __init__(self,  ai_settings,  screen):
        """Initialize the invader"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(self.ai_settings.invader_image)
        self.rect = self.image.get_rect()
        
        # start new invader near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # use float var to store the x position
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the invader"""
        self.screen.blit(self.image,  self.rect)
    
    def update(self):
        """Move the invader right"""
        self.x += ( self.ai_settings.invader_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """Return true if invader is on the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
