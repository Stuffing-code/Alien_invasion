class GameStats():
    """Class representing game statistics"""

    def __init__(self, ai_game):
        """Initializes the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """Initializes statistics, changing during the game."""
        self.ship_hit = self.settings.ship_hit
        self.invasions_kills = self.settings.invasions_kills
