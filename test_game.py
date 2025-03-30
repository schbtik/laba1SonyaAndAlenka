import pytest
from maze import Maze
from pacman import PacMan
from ghost import Ghost
from game_manager import GameManager
from game_state import GameState
from point import Point

# Тести для Maze
@pytest.fixture
def maze():
    return Maze()

def test_is_wall(maze):
    assert maze.is_wall(0, 0) is True
    assert maze.is_wall(1, 1) is False

def test_is_point(maze):
    assert maze.is_point(2, 1) is True
    assert maze.is_point(0, 0) is False

def test_eat_point(maze):
    assert maze.eat_point(2, 1) is True
    assert maze.grid[1][2] == ' '

# Тести для PacMan
@pytest.fixture
def game_manager(maze):
    return GameManager(maze)

@pytest.fixture
def pacman(game_manager):
    return PacMan(1, 1, game_manager)

def test_pacman_move(pacman, maze):
    pacman.move("RIGHT", maze)
    assert (pacman.x, pacman.y) == (2, 1)

def test_pacman_activate_power_mode(pacman):
    pacman.activate_power_mode()
    assert pacman.power_mode is True

def test_pacman_reset_position(pacman):
    pacman.move("RIGHT", Maze())
    pacman.reset_position()
    assert (pacman.x, pacman.y) == (1, 1)