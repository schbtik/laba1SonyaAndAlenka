import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Основний цикл гри
running = True
while running:
    screen.fill(BLACK)  # Очищення екрану
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()  # Оновлення екрану
    clock.tick(60)  # Обмеження FPS

pygame.quit()
sys.exit()