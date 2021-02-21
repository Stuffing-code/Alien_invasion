import sys

import pygame

from settings import Settings
from ship import Ship

class Raketa:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('RAKETA BOMB')

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    ai = Raketa()
    ai.run_game()
