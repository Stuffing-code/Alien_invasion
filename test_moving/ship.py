import pygame

class Ship():

    def __init__(self, r_game):
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        images = 'C:\\Users\\Stuffing\\Desktop\\lessons\\Alien_invasion\\test_moving\\images\\starship100x100.bmp'
        self.image = pygame.image.load(images)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_top and self.rect.top > 0:
            self.rect.y  -= 1
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)