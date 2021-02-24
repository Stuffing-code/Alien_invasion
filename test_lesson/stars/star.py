import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen
        self.settings = star_game.setting

        # Dowload images star.
        image_derectory = "C:\\Users\\Stuffing\\Desktop\\lessons\\Alien_invasion\\test_lesson\\stars\\star.bmp"
        self.image = pygame.image.load(image_derectory)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        self.y += self.settings.drop_speed
        self.rect.y = self.y