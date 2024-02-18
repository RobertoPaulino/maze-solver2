from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self._is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
 

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()
            
    def close(self):
        self._is_running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)