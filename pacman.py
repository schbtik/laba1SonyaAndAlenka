import time

class PacMan:
    def __init__(self, x, y, game_manager):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.game_manager = game_manager
        self.power_mode = False  # Чи активний енергоджайзер
        self.power_mode_end_time = 0

    def move(self, direction, maze):
        """Переміщення Pac-Man у заданому напрямку (заглушка)"""
        pass

    def activate_power_mode(self):
        """Активація енергоджайзера (заглушка)"""
        pass

    def update(self):
        """Оновлення стану Pac-Man (заглушка)"""
        pass

    def reset_position(self, start_x=1, start_y=1):
        """Скидає позицію Pac-Man у початкову (заглушка)"""
        pass