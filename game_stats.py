class GameStats():
    """
    Tracking statistics for game Alien Invasion.
    """

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        # Record dont need restarts.
        self.reset_stats()

        # Game Alien Invasion starting in active state.
        self.game_active = False

    def reset_stats(self):
        """Initializes statistics, changing during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = self.get_record()

    def get_record(self):
        with open("history_record.json", "r") as f:
            record = f.read()
            return int(record)
