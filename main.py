import pygame
import sys
from game_state import GameState
from maze import Maze
from game_manager import GameManager
from config import get_game_config

# Отримуємо колір лабіринту з конфіга
MAZE_COLOR = get_game_config()

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Створення гри
maze = Maze()
game = GameManager(maze)
game_state = GameState()

# малюємо лабіринт


def draw_maze():
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if cell == '#':  # Стіни
                pygame.draw.rect(
                    screen,
                    MAZE_COLOR,
                    (x * CELL_SIZE,
                     y * CELL_SIZE,
                     CELL_SIZE,
                     CELL_SIZE))
            elif cell == '.':  # Точки
                pygame.draw.circle(
                    screen,
                    WHITE,
                    (x *
                     CELL_SIZE +
                     CELL_SIZE //
                     2,
                     y *
                     CELL_SIZE +
                     CELL_SIZE //
                     2),
                    5)
            elif cell == 'O':  # Енергоджайзери
                pygame.draw.circle(
                    screen,
                    WHITE,
                    (x *
                     CELL_SIZE +
                     CELL_SIZE //
                     2,
                     y *
                     CELL_SIZE +
                     CELL_SIZE //
                     2),
                    10)


# Функція для малювання Pac-Man
def draw_pacman():
    pygame.draw.circle(
        screen,
        YELLOW,
        (game.pacman.x *
         CELL_SIZE +
         CELL_SIZE //
         2,
         game.pacman.y *
         CELL_SIZE +
         CELL_SIZE //
         2),
        CELL_SIZE //
        3)


# Функція для малювання привидів
def draw_ghosts():
    for ghost in game.ghosts:
        pygame.draw.rect(
            screen,
            ghost.color,
            (ghost.x *
             CELL_SIZE,
             ghost.y *
             CELL_SIZE,
             CELL_SIZE,
             CELL_SIZE))


# Функція для відображення рахунку та кількості життів
def draw_score_and_lives():
    font = pygame.font.Font(None, 36)

    # Рахунок
    score_text = font.render(f"Score: {game.pacman.score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Кількість життів
    lives_text = font.render(f"Lives: {game.pacman.lives}", True, WHITE)
    screen.blit(lives_text, (10, 50))  # Розташування тексту для життів

# Функція для перевірки зіткнення з привидом


def check_collision_with_ghosts():
    for ghost in game.ghosts:
        if game.pacman.x == ghost.x and game.pacman.y == ghost.y:
            if game.pacman.lives > 0:  # Якщо є життя для зменшення
                game.pacman.lives -= 1  # Зменшуємо кількість життів
                print(
                    f"Pac-Man з'їдений! Життів залишилось:"
                    f"{game.pacman.lives}")
                # Оновлюємо позицію Pac-Man (наприклад, на стартову)
                game.pacman.reset_position()
                if game.pacman.lives <= 0:
                    # Якщо немає життів, гра закінчується
                    game.game_over = True


# Основний цикл гри
running = True
while running:
    screen.fill(BLACK)  # Очищення екрану

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game.game_over:
            if event.key == pygame.K_UP:
                game.pacman.move("UP", maze)
            elif event.key == pygame.K_DOWN:
                game.pacman.move("DOWN", maze)
            elif event.key == pygame.K_LEFT:
                game.pacman.move("LEFT", maze)
            elif event.key == pygame.K_RIGHT:
                game.pacman.move("RIGHT", maze)

    check_collision_with_ghosts()  # Перевіряємо зіткнення з привидами

    game.update_game()  # Оновлення стану гри

    draw_maze()  # Малюємо лабіринт
    draw_pacman()  # Малюємо Pac-Man
    draw_ghosts()
    draw_score_and_lives()  # Відображаємо рахунок та кількість життів

    pygame.display.flip()  # Оновлення

    clock.tick(10)  # Обмеження FPS до 10

    # Якщо гра закінчена – зупиняємо цикл
    if game.game_over:
        running = False

pygame.quit()
sys.exit()
