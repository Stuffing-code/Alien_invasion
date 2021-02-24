import sys
import pygame

from setting import Settings
from star import Star
from random import randint

class Stars:

    def __init__(self):
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_starsky()

    def run_game(self):
        while True:
            self._check_event()
            self._update_star()
            self._update_screen()


    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_starsky(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.setting.screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)

        available_space_y = (self.setting.screen_height -
                                - (3 * star_height) - 300)
        number_rows = available_space_y // (2 * star_height)

        for number_row in range(number_rows):
            for star_numer in range(number_star_x):
                self._create_star(star_numer, number_row)

    def _create_star(self, star_number, number_row):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * number_row
        self.stars.add(star)

    def _update_star(self):
        self.stars.update()
        self._check_edge()

    def _check_edge(self):
        for star in self.stars.sprites():
            if star.check_edge():
                self._check_starsky()
                break

    def _check_starsky(self):
        for star in self.stars.sprites():
            star.rect.y += self.setting.drop_speed

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    star = Stars()
    star.run_game()