from graphics import *

win = GraphWin("2D Line Clipping", 800, 600)
center_x = win.getWidth() / 2
center_y = win.getHeight() / 2
x_min, y_min, x_max, y_max = 0, 0, 200, 100

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8


def draw_axes():
    x_axis = Line(Point(0, center_y), Point(win.getWidth(), center_y))
    y_axis = Line(Point(center_x, 0), Point(center_x, win.getHeight()))
    for axis in [x_axis, y_axis]:
        axis.setArrow("both")
        axis.setFill("black")
        axis.draw(win)


def compute_outcode(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code


def draw_clipped_line(x1, y1, x2, y2, color):
    line = Line(
        Point(center_x + x1, center_y - y1), Point(center_x + x2, center_y - y2)
    )
    line.setOutline(color)
    line.draw(win)


def clip_cohen_sutherland_direct(x1, y1, x2, y2):
    outcode1 = compute_outcode(x1, y1)
    outcode2 = compute_outcode(x2, y2)

    while True:
        if not (outcode1 | outcode2):
            draw_clipped_line(x1, y1, x2, y2, "red")
            break
        if outcode1 & outcode2:
            draw_clipped_line(x1, y1, x2, y2, "black")
            return

        x, y = 0, 0

        if outcode1 != INSIDE:
            outcode = outcode1
        else:
            outcode = outcode2

        if outcode & TOP:
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max
        elif outcode & BOTTOM:
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min
        elif outcode & RIGHT:
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max
        elif outcode & LEFT:
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min

        if outcode == outcode1:
            x1, y1 = x, y
            outcode1 = compute_outcode(x1, y1)
        else:
            x2, y2 = x, y
            outcode2 = compute_outcode(x2, y2)


def clip_cohen_sutherland_midpoint(x1, y1, x2, y2):
    len = (x2 - x1)(x2 - x1) + (y2 - y1)(y2 - y1)
    if len <= 1:
        return
    outcode1 = compute_outcode(x1, y1)
    outcode2 = compute_outcode(x2, y2)

    if not (outcode1 | outcode2):  # Both endpoints are inside the window
        draw_clipped_line(x1, y1, x2, y2, "red")
        return
    elif outcode1 & outcode2:  # Both endpoints are outside the boundary
        draw_clipped_line(x1, y1, x2, y2, "black")
        return  # This line should be completely discarded
    else:
        x_m = (x1 + x2) / 2
        y_m = (y1 + y2) / 2

        if (x_m == x_min) or (x_m == x_max) or (y_m == y_min) or (y_m == y_max):
            if outcode1 | INSIDE:
                draw_clipped_line(x_m, y_m, x2, y2, "red")
            else:
                draw_clipped_line(x_m, y_m, x2, y2, "black")

            if INSIDE | outcode2:
                draw_clipped_line(x1, y1, x_m, y_m, "red")
            else:
                draw_clipped_line(x1, y1, x_m, y_m, "black")
        else:
            clip_cohen_sutherland_midpoint(x1, y1, x_m, y_m)
            clip_cohen_sutherland_midpoint(x_m, y_m, x2, y2)


def clip_liang_barsky(x1, y1, x2, y2):
    t1, t2 = 0, 1
    dx = x2 - x1
    dy = y2 - y1

    p = [0] * 5
    q = [0] * 5
    r = [0] * 5

    p[1] = -dx
    p[2] = dx
    p[3] = -dy
    p[4] = dy

    q[1] = x1 - x_min
    q[2] = x_max - x1
    q[3] = y1 - y_min
    q[4] = y_max - y1

    for i in range(1, 5):
        if p[i] == 0:
            if q[i] < 0:
                print("Line is outside")
                print(x1, y1, x2, y2)
                draw_clipped_line(x1, y1, x2, y2, "black")
                return
        else:
            r[i] = q[i] / p[i]

    for i in range(1, 5):
        if p[i] < 0:
            t1 = max(t1, r[i])
        elif p[i] > 0:
            t2 = min(t2, r[i])

    if t1 < t2:
        print(x1, y1, x2, y2)
        draw_clipped_line(x1 + t1 * dx, y1 + t1 * dy, x1 + t2 * dx, y1 + t2 * dy, "red")


def draw_window():
    window_rect = Rectangle(
        Point(center_x + x_min, center_y - y_min),
        Point(center_x + x_max, center_y - y_max),
    )
    window_rect.setOutline("blue")
    window_rect.setWidth(2)
    window_rect.draw(win)


def main_menu():
    draw_axes()
    draw_window()
    lines = [
        (-50, -100, 100, 200),
        (15, 50, 150, 90),
        (205, 105, 250, 150),
        (100, -100, 100, 200),
        (-50, 100, -50, 400),
        (300, 200, 300, 100),
        (-100, 50, 300, 50),
        (-100, 150, 300, 150),
        (-100, -100, 300, -100),
    ]
    # for line in lines:
    #     draw_clipped_line(*line, "black")

    while True:
        print("Select Clipping Algorithm:")
        print("1. Cohen-Sutherland (Direct)")
        print("2. Cohen-Sutherland (Midpoint Subdivision)")
        print("3. Liang-Barsky")
        print("Q. Quit")

        choice = input("Enter your choice: ").capitalize()
        if choice == "1":
            for line in lines:
                clip_cohen_sutherland_direct(*line)

        elif choice == "2":
            for line in lines:
                clip_cohen_sutherland_midpoint(*line)

        elif choice == "3":
            for line in lines:
                win.getKey()
                clip_liang_barsky(*line)

        elif choice == "Q":
            break


if __name__ == "__main__":
    main_menu()
    win.getMouse()
    win.close()
