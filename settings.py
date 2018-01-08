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
        #kept from https://pixabay.com/it/razzo-vettoriale-spazio-lancio-2442125/
        #self.ship_image = 'images/rocket.bmp'
        self.ship_image = 'images/ship-invaders-2.bmp'
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 43
        self.bullet_allowed = 3
        # invader settings
        self.invader_image = 'images/invader.bmp'
