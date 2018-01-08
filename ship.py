import pygame

class Ship():
    """
    Define the best ship against the invaders :D
    """
    
    def __init__(self,  ai_settings,  screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(self.ai_settings.ship_image)
        self.rect = self.image.get_rect()
        # need to know the screen rectange dimension
        self.screen_rect = screen.get_rect()
        # start at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position"""
        if self.moving_right and ( self.rect.right < self.screen_rect.right ):
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and ( self.rect.left > 0 ):
            self.center -= self.ai_settings.ship_speed_factor
        
        # last update the centerx based on the self.center value
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,  self.rect)
