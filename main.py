import pygame
import sys
from game_state import GameState
from maze import Maze
from game_manager import GameManager

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

#рисуем стены
def draw_maze():
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if cell == '#':  # Стіни
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Основний цикл гри

# Основний цикл гри
running = True
while running:
    screen.fill(BLACK)  # Очищення екрану

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_maze()
    pygame.display.flip()  # Оновлення екрану
    clock.tick(60)  # Обмеження FPS

pygame.quit()
sys.exit()
