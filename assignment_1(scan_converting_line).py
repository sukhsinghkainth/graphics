########################################################################
# Assignment 1. Scan Converting Line
# (Direct Method, Parametric Method ,DDA Method ,Bresenham Method)
# Roll number: 22071293
# Name: Sukhpreet Singh Kainth
# Date: 29-08-2023
########################################################################


import graphics as gr
import time

# Test case line coordinates
lines = [
    (100, 100, 400, 200, "gold"),
    (100, 200, 400, 100, "aqua"),
    (400, 100, 100, 200, "springGreen"),
    (400, 200, 100, 100, "blue"),
    (100, 100, 200, 400, "aquamarine"),
    (100, 400, 200, 100, "blueViolet"),
    (200, 100, 100, 400, "brown"),
    (200, 400, 100, 100, "CadetBlue"),
    (100, 100, 400, 100, "burlywood"),
    (400, 100, 100, 100, "chartreuse"),
    (100, 100, 100, 200, "crimson"),
    (100, 200, 100, 100, "DarkgoldenRod"),
    (100, 100, 100, 100, "Darkblue"),
]

# Create a window
win = gr.GraphWin("Line Drawing", 1024, 768)
win.setBackground("black")


def linedraw(x, y, colors, win):
    pnt = gr.Point(x, y)
    pnt.setFill(colors)
    pnt.draw(win)
    time.sleep(0.01)


def linedrawbefore(x1, y1, x2, y2, win):
    l = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    l.setFill("white")
    l.draw(win)


# Function to draw lines using the Direct Method


def draw_direct(x1, y1, x2, y2, colors):
    dx = x2 - x1
    dy = y2 - y1
    adx, ady = abs(dx), abs(dy)
    if dx == 0 and dy == 0:
        linedraw(x1, y1, colors, win)
        return
    if adx == 0:
        x_inc = 0
    else:
        x_inc = dx / adx

    if ady == 0:
        y_inc = 0
    else:
        y_inc = dy / ady

    x, y = x1, y1

    linedrawbefore(x1, y1, x2, y2, win)
    linedraw(x, y, colors, win)

    if adx >= ady:
        m = dy / dx
        b = y1 - m * x1
        while x != x2:
            x = x + x_inc
            y = m * x + b
            linedraw(x, y, colors, win)
    else:
        if dx == 0:
            while y != y2:
                y = y + y_inc
                linedraw(x, y, colors, win)
            return

        m = dy / dx
        m_inv = 1 / m
        b = y1 - m * x1
        while y != y2:
            y = y_inc + y
            x = m_inv * (y - b)
            linedraw(x, y, colors, win)


# Function to draw lines using the Parametric Method
def draw_parametric(x1, y1, x2, y2, colors):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    linedrawbefore(x1, y1, x2, y2, win)

    if steps == 0:
        u_inc = 1
    elif steps == abs(dx):
        u_inc = 1 / steps
    else:
        u_inc = 1 / steps

    u = 0
    x, y = x1, y1
    linedraw(x, y, colors, win)

    while u <= 1:
        u += u_inc
        x = x1 + u * dx
        y = y1 + u * dy
        linedraw(x, y, colors, win)


# Function to draw lines using the DDA Method
def draw_dda(x1, y1, x2, y2, colors):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    if steps == 0:
        x_inc = 0
        y_inc = 0
    else:
        x_inc = dx / steps
        y_inc = dy / steps
    linedrawbefore(x1, y1, x2, y2, win)

    x, y = x1, y1
    linedraw(x, y, colors, win)
    k = 1
    while k != steps:
        x, y = x + x_inc, y + y_inc
        k += 1
        linedraw(x, y, colors, win)


# Function to draw lines using the Bresenham Method
def draw_bresenham(x1, y1, x2, y2, colors):
    linedrawbefore(x1, y1, x2, y2, win)
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    adx = abs(dx)
    ady = abs(dy)

    if dx == 0:
        xinc = 0
    else:
        xinc = dx / adx

    if dy == 0:
        yinc = 0
    else:
        yinc = dy / ady

    if adx > ady:
        p = 2 * ady - adx
        while x != x2:
            if p < 0:
                p = p + 2 * ady
            else:
                p = p + 2 * ady - 2 * adx
                y = y + yinc
            x = x + xinc
            linedraw(x, y, colors, win)
    else:
        p = 2 * adx - ady
        while y != y2:
            if p < 0:
                p = p + 2 * adx
            else:
                p = p + 2 * adx - 2 * ady
                x = x + xinc
            y = y + yinc
            linedraw(x, y, colors, win)


# Draw lines using the selected method
def draw_lines(method):
    for x1, y1, x2, y2, colors in lines:
        if method == 1:
            draw_direct(x1, y1, x2, y2, colors)
        elif method == 2:
            draw_parametric(x1, y1, x2, y2, colors)
        elif method == 3:
            draw_dda(x1, y1, x2, y2, colors)
        elif method == 4:
            draw_bresenham(x1, y1, x2, y2, colors)


# Get user input for method choice
print("Select a method to draw lines:")
print("1. Direct Method") 
print("2. Parametric Method")
print("3. DDA Method") 
print("4. Bresenham Method")
method_choice = int(input())

# Draw lines using the selected method
draw_lines(method_choice)

# Wait for a click before closing the window
win.getMouse()
win.close()
