class Settings():
    """
    A class to store all settings for Space invaders.
    """
    
    def __init__(self):
        """Initialize the game's settings"""
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,  230,  230)
        self.caption = "Amedeo version of Space Invaders"
        self.ship_image = 'images/ship.bmp'
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,  60,  60
