class Settings():
    """Class to store all game settings Alien Invasion."""
    def __init__(self):
        """
        Initializes settings game.
        """
        # Screen settings.
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (176, 224, 230)

        #Settings ship.
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Settings projectile.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60 , 60)
        self.bullets_allowed = 3

        # Settings aliens.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction = 1 indicates movement to right; and - 1 to the left
        self.fleet_direction = 1