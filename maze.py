from cell import Cell
import time, random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = (self._x1) + (i * self._cell_size_x)
        cell_y1 = (self._y1) + (j * self._cell_size_y)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.015)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            possible_move = []
            move = "None"

            #Check cell to the right
            if i < self._num_cols - 1:
                if self._cells[i + 1][j]._visited == False:
                    possible_move.append((i+1,j))
                    
            
            #Check cell to the left
            if i > 0:
                if self._cells[i - 1][j]._visited == False:
                    possible_move.append((i-1, j))
                    

            #Check cell above
            if j > 0:
                if self._cells[i][j - 1]._visited == False:
                    possible_move.append((i, j-1))
                    

            #Check cell below
            if j < self._num_rows-1:
                if self._cells[i][j + 1]._visited == False:
                    possible_move.append((i,j+1))
                    

            if len(possible_move) == 0:
                self._draw_cell(i,j)
                return
            
            goal = possible_move[random.randint(0,len(possible_move)-1)]
            #determine the direction taken
            if goal[0] == i:
                if goal[1] > j:
                    move = 'd'
                else:
                    move = 'u'
            else:
                if goal[0] > i:
                    move = 'r'
                else:
                    move = 'l'
    
            self._update_walls(self._cells[i][j], self._cells[goal[0]][goal[1]], move)
            self._break_walls_r(goal[0], goal[1])
            
    def _update_walls(self, current, goal, dir):
        if dir == 'u':
            goal.has_bottom_wall = False
            current.has_top_wall = False
        elif dir == 'd':
            goal.has_top_wall = False
            current.has_bottom_wall = False
        elif dir == 'l':
            goal.has_right_wall = False
            current.has_left_wall = False
        elif dir == 'r':
            goal.has_left_wall = False
            current.has_right_wall = False
        else:
            raise Exception(f"Error in the direction provided to wall update function, received: {dir}")