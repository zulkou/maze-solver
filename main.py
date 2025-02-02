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

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )


def main():
    win = Window(800, 600)
    point1 = Point(200, 300)
    point2 = Point(600, 300)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
