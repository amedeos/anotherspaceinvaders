class Settings():
    """
    A class to store all settings for Space invaders.
    """
    
    def __init__(self):
        """Initialize the game's settings"""
        # screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,  230,  230)
        self.caption = "Amedeo version of Space Invaders"
        #kept from https://pixabay.com/it/razzo-vettoriale-spazio-lancio-2442125/
        #self.ship_image = 'images/rocket.bmp'
        self.ship_image = 'images/ship-invaders-2.bmp'
        self.ship_left = 1
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 43
        self.bullet_allowed = 3
        # invader settings
        self.invader_image = 'images/invader-2.bmp'
        self.invader_height_factor = 5
        self.invader_width_factor = 3
        self.fleet_drop_speed = 10
        
        self.sleep_second = 1
        
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1.5
        self.invader_speed_factor = 0.5
        
        # 1 -> right ; -1 -> left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.invader_speed_factor *= self.speedup_scale
