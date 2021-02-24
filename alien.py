import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing one alien."""

    def __init__(self, ai_game):
        """
        initializes the alien and sets its initial position.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Dowload alien image and appointment atr rect.
        self.image = pygame.image.load('images/invasion.bmp')
        self.rect = self.image.get_rect()

        # New alien position.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save alien position horizontally.
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Reterns True, if alien is at the edge of the screen.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien to right or left."""
        self.x += (
            self.settings.alien_speed * self.settings.fleet_direction
        )
        self.rect.x = self.x
