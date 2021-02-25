class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 210, 230)
        
        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        # Alien settings.
        self.invasion_speed = 0.5
        self.fleet_drop_speed = 3
        # fleet_direction = 1 indicates movement to right, and -1 to the left.
        self.fleet_direction = 1

        # Ship settings.
        self.ship_hit = 0
        self.invasions_kills = 0

