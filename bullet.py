import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to control the rockets fired by the ship."""

    def __init__(self, ai_game):
        """
        Create the object of the projectile in the current position of the ship.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #Create projectile in position (0, 0)  and correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Position projectile save in float type.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the projectile up the screen."""
        #Update position of projectile in float type.
        self.y -= self.settings.bullet_speed
        #Update position of rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw projectile in the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
