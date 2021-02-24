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

        # Dowload alien image and appointment atr rect.
        self.image = pygame.image.load('images/invasion.bmp')
        self.rect = self.image.get_rect()

        # New alien position.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save alien position horizontally.
        self.x = float(self.rect.x)
        