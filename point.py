class Point:
    def __init__(self, x: int, y: int, is_power_up: bool = False):
        """Точка, яку може збирати Pac-Man"""
        self.x = x
        self.y = y
        self.is_power_up = is_power_up  # Якщо точка є енергетичною

    def consume(self):
        """Pac-Man з'їдає точку"""
        return 10 if not self.is_power_up else 50  # Звичайна точка = 10, енергетична = 50
