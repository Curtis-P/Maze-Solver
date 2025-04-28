from cell import Cell
import random
import time


class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win = None, seed = None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    
    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):               
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        #calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself.
        if self._win is None:
            return
        x1 = self._x1 + (i*self._cell_size_x)
        y1 = self._y1 + (j*self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols -1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        #mark current cell as visited
        self._cells[i][j].visited = True
        #infinite loop
        while True:
            to_be_visited = []
            #possible visit directions
            #i = horrizontal j = verticle
            #left
            if i > 0 and not self._cells[i-1][j].visited:
                to_be_visited.append((i-1, j))
            #right
            if i < (self._num_cols -1) and not self._cells[i+1][j].visited:
                to_be_visited.append((i+1,j))
            #up
            if j > 0 and not self._cells[i][j-1].visited:
                to_be_visited.append((i, j-1))
            #down
            if j < (self._num_rows -1) and not self._cells[i][j+1].visited:
                to_be_visited.append((i, j+1))
            if len(to_be_visited) == 0:
                self._draw_cell(i,j)
                return
            next_cell_index = random.randrange(len(to_be_visited))
            next_cell_tupple = to_be_visited[next_cell_index]
            if next_cell_tupple[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next_cell_tupple[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_cell_tupple[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_cell_tupple[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            self._break_walls_r(next_cell_tupple[0], next_cell_tupple[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        if self._solve_r(0,0):
            return True
        else:
            return False
        
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        to_be_visited = []
        #possible visit directions
        #i = horrizontal j = verticle
        #left
        if i > 0 and not self._cells[i-1][j].has_right_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            check = self._solve_r(i-1, j)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        #right
        if i < (self._num_cols -1)and not self._cells[i+1][j].has_left_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            check = self._solve_r(i+1, j)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
            
        #up
        if j > 0 and not self._cells[i][j-1].has_bottom_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            check = self._solve_r(i, j-1)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        #down
        if j < (self._num_rows -1) and not self._cells[i][j+1].has_top_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            check = self._solve_r(i, j+1)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        
        return False
            
        