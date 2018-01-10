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
        self.ship_speed_factor = 0.5
        self.ship_left = 1
        # bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 43
        self.bullet_allowed = 3
        # invader settings
        self.invader_image = 'images/invader-2.bmp'
        self.invader_speed_factor = 1
        self.invader_height_factor = 5
        self.invader_width_factor = 3
        self.fleet_drop_speed = 10
        # 1 -> right ; -1 -> left
        self.fleet_direction = 1
        self.sleep_second = 1
