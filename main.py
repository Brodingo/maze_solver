from graphics import Window
from maze import Maze


def main():

    num_rows = 10
    num_cols = 12
    margin = 50
    screen_x = 1024
    screen_y = 768
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    # p1 = Point(100, 100)
    # p2 = Point(100, 200)
    # p3 = Point(200, 200)
    # l1 = Line(p1, p2)
    # l2 = Line(p2, p3)

    # win.draw_line(l1, "red")
    # win.draw_line(l2, "green")

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(100, 100, 200, 200)

    # c2 = Cell(win)
    # c2.has_right_wall = False
    # c2.draw(200, 100, 300, 200)

    # c3 = Cell(win)
    # c3.has_bottom_wall = False
    # c3.draw(100, 200, 200, 300)

    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(100, 100, 200, 200)

    # c2.draw_move(c)
    # c3.draw_move(c4, True)



    win.wait_for_close()


main()