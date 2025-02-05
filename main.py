from tkinter import Tk, BOTH, Canvas


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
    def __init__(self, x1, x2, y1, y2, win):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

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


def main():
    win = Window(800, 600)

    point1 = Point(200, 300)
    point2 = Point(600, 300)
    line = Line(point1, point2)

    cell1 = Cell(350, 400, 250, 300, win)
    cell1.draw()
    cell2 = Cell(400, 450, 250, 300, win)
    cell2.draw()
    cell3 = Cell(350, 400, 300, 350, win)
    cell3.draw()
    cell4 = Cell(400, 450, 300, 350, win)
    cell4.draw()

    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
