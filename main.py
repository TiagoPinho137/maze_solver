from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    l = Line(Point(300, 300), Point(-400, 400))
    win.draw_line(l, "black")
    win.wait_for_close()


main()
