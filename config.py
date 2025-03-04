import argparse

def get_game_config():
    parser = argparse.ArgumentParser(description="Pac-Man Game Settings")
    parser.add_argument("--maze_color", default="blue", help="Колір лабіринту (наприклад, 'blue', 'red', 'green')")

    args = parser.parse_args()

    color_map = {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255)
    }

    return color_map.get(args.maze_color.lower(), (0, 0, 255))  # За замовчуванням синій
