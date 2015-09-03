"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    my_line = list(line)
    for idx1 in range(len(my_line)):
        if my_line[idx1] == 0:
            continue
        idx2 = idx1 + 1
        while idx2 < len(my_line) and my_line[idx2] == 0:
            idx2 += 1
        if idx2 < len(my_line) and my_line[idx1] == my_line[idx2]:
            my_line[idx1] += my_line[idx1]
            my_line[idx2] = 0
        idx2 = idx1
        while idx2 > 0 and my_line[idx2 - 1] == 0:
            idx2 -= 1
        if idx1 != idx2:
            my_line[idx2] = my_line[idx1]
            my_line[idx1] = 0
    return my_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._cells = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        row_dir = OFFSETS[direction][0]
        col_dir = OFFSETS[direction][1]
        
        if row_dir == 0:
            new_cells = self._cells
            new_dir = col_dir
        else:
            new_tuples = zip(*self._cells)
            new_cells = [list(item) for item in new_tuples]
            new_dir = row_dir
        
        tmp_cells = []
        for lists in new_cells:
            lists = lists[::new_dir]
            merge_lists = merge(lists)
            tmp_cells.append(merge_lists[::new_dir])
            
        if row_dir == 0:
            self._cells = tmp_cells
        else:
            new_tuples = zip(*tmp_cells)
            new_cells = [list(item) for item in new_tuples]
            self._cells = new_cells
            
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        empty_square_lists = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if(self.get_tile(row, col) == 0):
                    empty_square_lists.append((row, col))
        
        if len(empty_square_lists) == 0:
            return "game over!"
            
        random_cell = random.choice(empty_square_lists)
        random_cell_row = random_cell[0]
        random_cell_col = random_cell[1]
        
        values = [2] * 90 + [4] * 10
        value = random.choice(values)
        
        self.set_tile(random_cell_row, random_cell_col, value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._cells[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
