import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to control rhe rockets fired by the ship."""


    def __init__(self, r_game):
        """Create the object of the projectile in the current position."""
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.color = r_game.settings.bullet_color

        # Create projectile position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = r_game.ship.rect.midright

        # Position projectille save in float type.
        self.x = float(self.rect.x)

    def update(self):
        """Moves the projectile projectile right to screen."""
        self.x += self.settings.bullet_speed
        # Update position of the projectile.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw projectile in the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)