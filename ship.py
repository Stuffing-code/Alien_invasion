import pygame

class Ship():
    """Ship control class"""

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image of the ship and receives a rectangle.
        self.image = pygame.image.load('images/starship100x100.bmp')
        self.rect = self.image.get_rect()
        # Every new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the ship in current position."""
        self.screen.blit(self.image, self.rect)
