from line import Point, Line
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        #create points to avoid confusion
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        

        #check if there is a left wall
        #create the Line() and draw it.
        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)
            
        #check if there is a right wall
        #create the Line() and draw it.
        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)
            

        #check if there is a left wall
        #create the Line() and draw it.
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)

        #check if there is a left wall
        #create the Line() and draw it.
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall)
            