class GameStats():
    """
    Store statistics
    """
    def __init__(self,  ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        self.high_score = 0
    
    def reset_stats(self):
        """IReset all statistics"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.ai_settings.invader_points = 50
        self.level = 1
