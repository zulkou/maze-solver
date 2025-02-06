from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")

        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()

        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall= True, has_bottom_wall=True):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self.center_x = (self._x1 + self._x2) / 2
        self.center_y = (self._y1 + self._y2) / 2

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            line.draw(self._win.canvas)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            line.draw(self._win.canvas)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            line.draw(self._win.canvas)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            line.draw(self._win.canvas)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "grey"
        else:
            color = "red"

        if not self.has_left_wall and not to_cell.has_right_wall:
            line = Line(Point(self.center_x, self.center_y), Point(to_cell.center_x, to_cell.center_y))
            line.draw(self._win.canvas, color)
        if not self.has_right_wall and not to_cell.has_left_wall:
            line = Line(Point(self.center_x, self.center_y), Point(to_cell.center_x, to_cell.center_y))
            line.draw(self._win.canvas, color)
        if not self.has_top_wall and not to_cell.has_bottom_wall:
            line = Line(Point(self.center_x, self.center_y), Point(to_cell.center_x, to_cell.center_y))
            line.draw(self._win.canvas, color)
        if not self.has_bottom_wall and not to_cell.has_top_wall:
            line = Line(Point(self.center_x, self.center_y), Point(to_cell.center_x, to_cell.center_y))
            line.draw(self._win.canvas, color)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(
                    Cell(
                        self._x1 + i*self._cell_size_x, 
                        self._x1 + (i+1)*self._cell_size_x, 
                        self._y1 + j*self._cell_size_y, 
                        self._y1 + (j+1)*self._cell_size_y,
                        self._win
                    )
                )
            self._cells.append(column)
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

def main():
    win = Window(800, 600)

    # point1 = Point(200, 300)
    # point2 = Point(600, 300)
    # line = Line(point1, point2)
    # win.draw_line(line, "black")

    # cell1 = Cell(350, 400, 250, 300, win, has_right_wall=False)
    # cell1.draw()
    # cell2 = Cell(400, 450, 250, 300, win, has_left_wall=False, has_bottom_wall=False)
    # cell2.draw()
    # cell3 = Cell(350, 400, 300, 350, win, has_right_wall=False)
    # cell3.draw()
    # cell4 = Cell(400, 450, 300, 350, win, has_left_wall=False, has_top_wall=False)
    # cell4.draw()

    # cell1.draw_move(# cell2)
    # cell2.draw_move(# cell4)
    # cell4.draw_move(# cell3)
    maze = Maze(50, 50, 4, 5, 20, 20, win)
    maze._create_cells()

    win.wait_for_close()


if __name__ == "__main__":
    main()
