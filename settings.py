class Settings:
    """A class to store all setting for example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (238,238,228)
        # ship settings
        self.ship_speed_factor = 0.5
        # bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 64, 64, 64
        self.bullets_allowed = 3
        # aliens settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 5
        # fleet derection right = 1, left = -1
        self.fleet_direction = 1