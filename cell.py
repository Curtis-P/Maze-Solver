from graphics import Line, Point

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "#d9d9d9")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "#d9d9d9")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        #solving the simplest implementation of this assuming that the cells are across from one another
        # find center of self
        # find center of to cell
        #draw line with color from self.center -> to_cell.center
        def find_center(cell):
            center_x = ((cell._x2 - cell._x1) // 2) + cell._x1
            center_y = ((cell._y2 - cell._y1) // 2) + cell._y1
            center_point = Point(center_x, center_y)
            return center_point
        from_center_point = find_center(self)
        to_center_point = find_center(to_cell)

        line = Line(from_center_point, to_center_point)

        if undo:
            color = "gray70"
        else:
            color = "red"
        
        self._win.draw_line(line, color)
