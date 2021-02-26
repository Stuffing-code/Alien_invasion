class Settings():
    """Class to store all game settings Alien Invasion."""
    def __init__(self):
        """
        Initializes statistics settings game.
        """
        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (176, 224, 230)

        #Settings ship.
        self.ship_limit = 3

        #Settings projectile.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60 , 60)
        self.bullets_allowed = 3

        # Settings aliens.
        self.fleet_drop_speed = 10
        # fleet_direction = 1 indicates movement to right; and - 1 to the left
        self.fleet_direction = 1

        # Game speed.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings, changing in the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        # fleet_direction = 1 indicates movement to right; and - 1 to the left
        self.fleet_direction = 1

        # Calculate point
        self.alien_points = 50

    def increase_speed(self):
        """Increase settings speed and value aliens."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
