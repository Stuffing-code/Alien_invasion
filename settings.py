class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """
        Инициализирует настройки игры.
        """
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 760
        self.bg_color = (176, 224, 230)

        #Settings ship
        self.ship_speed = 1.5