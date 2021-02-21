class Settings():
    """Class to store all game settings Alien Invasion."""
    def __init__(self):
        """
        Initializes settings game
        """
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 450
        self.bg_color = (176, 224, 230)

        #Settings ship
        self.ship_speed = 0.6

        #Settings projectile
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60 , 60)
        self.bullets_allowed = 3
