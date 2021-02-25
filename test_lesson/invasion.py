import pygame
from pygame.sprite import Sprite

class Invasion(Sprite):
    """Class representing invasion."""

    def __init__(self, ai_game):
        """Initializes the invasion and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Dowload invasions image and appointment atr rect.
        image_directory = "C:\\Users\\Stuffing\\Desktop\\lessons\\Alien_invasion\\test_lesson\\images\\invasion.bmp"
        self.image = pygame.image.load(image_directory)
        self.rect = self.image.get_rect()

        # New invasion position.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.topright = self.screen_rect.topright

        # Save invasion position in vertikal
        self.y = float(self.rect.y)

    def check_edge(self):
        """Reterns True invasion is at the edge of the screen."""

        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """
        Moves invasion to bottom or top of screen.
        """
        self.y += (
            self.settings.invasion_speed * self.settings.fleet_direction
        )
        self.rect.y = self.y
