class Maze: 
    def __init__(self): 
        self.grid = [ 
            list("###############"), 
            list("#P..O.....#...#"), 
            list("#.#######.#.#.#"), 
            list("#.#     #.#  .#"), 
            list("#.# ### #.#  .#"), 
            list("#.#   # #.GG..#"), 
            list("#.### # #####.#"), 
            list("#.....#.......#"), 
            list("#####.#.#####.#"), 
            list("#.....#.#    .#"), 
            list("#.#####.# ## .#"), 
            list("#.....#.# ## .#"), 
            list("#.#####.####..#"), 
            list("#O............#"), 
            list("###############") 
        ] 
 
    def is_wall(self, x, y): 
        """Перевіряє, чи є стіна на координатах (x, y)""" 
        return self.grid[y][x] == '#' 
 
    def is_point(self, x, y): 
        """Перевіряє, чи є точка у комірці""" 
        return self.grid[y][x] == '.' 
 
    def is_power_pellet(self, x, y): 
        """Перевіряє, чи є енергоджайзер у комірці""" 
        return self.grid[y][x] == 'O'