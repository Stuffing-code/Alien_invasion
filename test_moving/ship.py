import pygame

class Ship():

    def __init__(self, r_game):
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        self.image = pygame.image.load('images/starship100x100.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.moving_top and self.rect.top > 0:
            self.rect.y  -= 1
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)