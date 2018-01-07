import pygame

class Ship():
    """
    Define the best ship against the invaders :D
    """
    
    def __init__(self,  screen,  ship_image='images/ship.bmp'):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.image = pygame.image.load(ship_image)
        self.rect = self.image.get_rect()
        # need to know the screen rectange dimension
        self.screen_rect = screen.get_rect()
        # start at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,  self.rect)
