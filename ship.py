import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Ship control class"""

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image of the ship and receives a rectangle.
        self.image = pygame.image.load('images/starship100x100.bmp')
        self.rect = self.image.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float coordinates centered ship.
        self.x = float(self.rect.x)

        # Flags moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates ship position to flag."""
        # Updates atr x, nor rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update atr rect atr based on self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship in current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place ship in the midottom in the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
