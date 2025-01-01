from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    # p1 = Point(100, 100)
    # p2 = Point(100, 200)
    # p3 = Point(200, 200)
    # l1 = Line(p1, p2)
    # l2 = Line(p2, p3)

    # win.draw_line(l1, "red")
    # win.draw_line(l2, "green")

    cell = Cell(100, 100, 200, 200, win, [True, True, False, True])
    cell2 = Cell(200, 100, 300, 200, win, [True, False, False, True])
    cell3 = Cell(300, 100, 400, 200, win, [False, True, True, False])

    cell.draw()
    cell2.draw()
    cell3.draw()

    win.wait_for_close()


main()