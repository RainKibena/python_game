class GameStats():
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.reset_stats()
    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit