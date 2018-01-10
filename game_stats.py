class GameStats():
    """
    Store statistics
    """
    def __init__(self,  ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
    
    def reset_stats(self):
        """IReset all statistics"""
        self.ship_left = self.ai_settings.ship_left
