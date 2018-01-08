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
