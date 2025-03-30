from game_state import GameState
from pacman import PacMan
from ghost import Ghost


class GameManager:
    def __init__(self, maze):
        self.pacman = PacMan(1, 1, self)
        self.ghosts = [Ghost(6, 5), Ghost(8, 5), Ghost(10, 5)]
        self.maze = maze
        self.game_state = GameState()
        self.game_over = False

    def update_game(self):
        """Оновлення гри після кожного кроку"""
        if self.game_over:
            return

        for ghost in self.ghosts:
            ghost.update(self)  # Оновлюємо стан привидів
            ghost.move(self.maze)  # Рухаємо привидів

        # Перевірка зіткнення Pac-Man з привидами
        if any(g.x == self.pacman.x and g.y ==
               self.pacman.y for g in self.ghosts):
            if self.pacman.power_mode:
                print("🌀 Pac-Man з'їв привида!")
                self.pacman.update()  # Оновлення стану Pac-Man
                for ghost in self.ghosts:
                    if ghost.x == self.pacman.x and ghost.y == self.pacman.y:
                        # Повертаємо привида на стартову позицію
                        ghost.x, ghost.y = 6, 5
                        ghost.eatable = False
                        ghost.color = (255, 0, 0)  # Привид знову стає червоним
                        self.pacman.score += 200
            else:
                print(f"❌ Pac-Man з'їдений! Життів залишилось: "
                      f"{self.pacman.lives - 1}")

                self.pacman.lives -= 1
                if self.pacman.lives <= 0:
                    self.game_over = True
                    print("❌ ГРА ЗАКІНЧЕНА! Pac-Man програв!")
                    return

        # Перевірка перемоги
        if self.check_win_condition():
            self.game_over = True
            print("🎉 ВІТАЄМО! Pac-Man виграв!")

    def check_win_condition(self):
        """Перевіряє, чи всі точки зібрані"""
        for row in self.maze.grid:
            if '.' in row or 'O' in row:
                return False
        return True
