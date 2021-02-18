import sys

import pygame

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        # назначение цвета фона.
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Запуск основго цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходу цикла перерисовывается экран.
            self.screen.fill(self.bg_color)

            # Отоброжение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
