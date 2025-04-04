import random
import time


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.previous_tile = ' '
        self.eatable = False
        self.color = (255, 0, 0)  # Червоний за замовчуванням
        # Час, коли привид повернеться до нормального стану
        self.eatable_timer = 0

    def update(self, game_manager):
        """Оновлення стану привидів (чи їстівні вони)"""
        if game_manager.pacman.power_mode:
            if not self.eatable:
                self.eatable = True
                self.color = (0, 255, 0)  # Привид стає синім
                self.eatable_timer = game_manager.pacman.power_mode_end_time
        elif self.eatable and time.time() > self.eatable_timer:
            print("🔴 Привид повернувся до звичайного стану!")
            self.eatable = False
            self.color = (255, 0, 0)  # Привид повертається в червоний колір

    def move(self, maze):
        """Рух привида випадковим напрямком"""
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        random.shuffle(directions)

        for direction in directions:
            new_x, new_y = self.x, self.y
            if direction == "UP":
                new_y -= 1
            elif direction == "DOWN":
                new_y += 1
            elif direction == "LEFT":
                new_x -= 1
            elif direction == "RIGHT":
                new_x += 1

            if not maze.is_wall(new_x, new_y):  # Якщо немає стіни
                # Відновлюємо попередній об'єкт у клітинці
                maze.grid[self.y][self.x] = self.previous_tile
                # Запам'ятовуємо, що було в новій клітинці
                self.previous_tile = maze.grid[new_y][new_x]
                self.x, self.y = new_x, new_y  # Переміщаємо привида
                # Встановлюємо привида в новій клітинці
                maze.grid[self.y][self.x] = 'G'
                break  # Вийти після успішного руху
