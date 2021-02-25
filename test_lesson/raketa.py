import sys

import pygame

from settings import Settings
from ship import Ship
from bullets import Bullet
from invasion import Invasion

class Raketa:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('RAKETA BOMB')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.invasions = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_invasions()
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
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = False

    def _create_fleet(self):
        invasion = Invasion(self)
        invasion_width, invasion_height = invasion.rect.size
        avaible_spece_y = self.settings.screen_height - (2 * invasion_height)
        number_invasion = avaible_spece_y // (2 * invasion_height)

        ship_with = self.ship.rect.width
        avaible_space_x = (self.settings.screen_width + (invasion_width) - ship_with)
        nubmers_row = avaible_space_x // (2 * invasion_width)

        # Create row invasion.
        for row_number in range(nubmers_row - 1):
            for invasion_number in range(number_invasion):
                self._create_invasaion(invasion_number, row_number)

    def _create_invasaion(self, invasion_number, row_number):
        invasion = Invasion(self)
        invasion_width, invasion_height = invasion.rect.size
        invasion.y = invasion_height + 2 * invasion_height * invasion_number
        invasion.rect.y = invasion.y

        invasion.rect.x = (
            (invasion.rect.width + 2 * invasion.rect.width * 
            (row_number + 2)))

        self.invasions.add(invasion)

    def _check_fleet_edges(self):
        for invasion in self.invasions.sprites():
            if invasion.check_edge():
                self._change_edge_direction()
                break

    def _change_edge_direction(self):
        for invasion in self.invasions.sprites():
            invasion.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullets(self):
        """Create the projectile and include it in the group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position projectile and delete old projectile."""
        # Update position
        self.bullets.update()

        # Delete projectile, beyond the edge of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_invasion_collisions()

    def _update_invasions(self):
        """
        Update position all invasions in fleet.
        """
        self._check_fleet_edges()
        self.invasions.update()

    def _check_bullet_invasion_collisions(self):
        """
        Handing of collisions of bullets with invasions.
        """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.invasions, True, True
        )
        if not self.invasions:
            # Destroy bullet and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.invasions.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    ai = Raketa()
    ai.run_game()
