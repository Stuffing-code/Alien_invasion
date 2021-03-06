import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Class for кesource and game behaviour."""

    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        # Creating an instance to store game statistics
        # and score board.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Created button Play.
        self.play_button = Button(self, "PLAY")

    def run_game(self):
        """Start the basic game cycle."""
        while True:
            self._check_event()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_event(self):
        """Handles keystrokes and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._write_record(self.stats.high_score)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _start_game(self):
        """Statrting game"""
        # Restart gme statisticians.
        self.stats.reset_stats()
        self.stats.game_active = True
        
        self._prep_images()

        # Clearing lists aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Restarting game settings.
        self.settings.initialize_dynamic_settings()

        # Creating new fleet and placment ship in the middle.
        self._create_fleet()
        self.ship.center_ship()
        
        # The mouse pointer is hidden.
        pygame.mouse.set_visible(False)

    def _prep_images(self):
        """Preparation images score"""
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

    def _start_new_lewel(self):
        """Starting new game with new settings."""
        self.settings.increase_speed()

        # Increased level.
        self.stats.level += 1
        self.sb.prep_level()

    def _check_play_button(self, mouse_pos):
        """Played new game if down button 'PLAY'"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()


    def _check_keydown_event(self, event):
        """Reacts when keys are released."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_1:
            self.settings.ship_speed = 1.5
            self.settings.bullet_speed = 2.0
            self.settings.alien_speed = 1.0
        elif event.key == pygame.K_2:
            self.settings.ship_speed = 1.5
            self.settings.bullet_speed = 3.0
            self.settings.alien_speed = 2.0
        elif event.key == pygame.K_3:
            self.settings.ship_speed = 2.5
            self.settings.bullet_speed = 3.5
            self.settings.alien_speed = 3.0
        elif event.key == pygame.K_q:
            self._write_record(self.stats.high_score)
            sys.exit()

    def _check_keyup_event(self, event):
        """Reacts when keys are released."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create the projectile and include it in the group 'bullets'."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Update position projectiles and delete old projectile.
        """
        # Update position projectile.
        self.bullets.update()

        # Delete projectiles, beyond the edge of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        """Update postions all aliens in fleets."""
        self._check_fleet_edges()
        self.aliens.update()

        # Checking, did the aliens get to the bottom of the screen
        self._check_aliens_bottom()

        # Collision check 'Alien - Ship '
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_bullet_alien_collisions(self):
        """Handing of collisions of projectile with aliens."""
        # Alien check
        # Remove projectile and alien on impact.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destroy projectile and create new fleet.
            self.bullets.empty()
            self._create_fleet()

            # Start level with new difficulty
            self._start_new_lewel()

    def _create_fleet(self):
        """Create fleet invasions"""
        # Create aliens and calculation of the number in the row.
        # The interval between neighboring aliens is equal to the width of the alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determines the number of rows to be placed on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create fleet invasions.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """
        Create alien and arranging him in the row.
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """
        React to the aliens reaching the edge of the screen.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Lowers the entire fleet and change the direction of the fleet.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Checking, did the aliens get to the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same thing happens when you hit a ship.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Handles a ship collision with an alien."""
        if self.stats.ships_left > 0:
            # Lowers ship_left and update score board.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Clearing lists aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Creating new fleet and placment ship in the middle.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _write_record(self, record):
        """Write record in file."""
        with open('history_record.json', 'w') as f:
            f.write(str(record))

    def _update_screen(self):
        """Updates the images on the screen and browses the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Output info score.
        self.sb.show_score()

        # Button Play draw if game not active.
        if not self.stats.game_active:
                self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion() # Create and start a game.
    ai.run_game()
