########################################################################
# Assignment 7: Projection
# Roll number: 22071225 , 22071226
# Name: Navpreet kaur , Shubham 
# Date: 06-11-2023
########################################################################

from graphics import *
import numpy as np

win = GraphWin("PROJECTION", 1200, 600)
mid_x = win.getWidth() / 2
mid_y = win.getHeight() / 2

w = 100


def draw_axes():
    x_axis = Line(Point(0, mid_y), Point(win.getWidth(), mid_y))
    y_axis = Line(Point(mid_x, 0), Point(mid_x, win.getHeight()))
    z_axis = Line(Point(0, win.getHeight()), Point(mid_x, mid_y))
    for axis in [x_axis, y_axis, z_axis]:
        axis.setFill("black")
        axis.draw(win)


pyramid_coordinates = np.array([[0, w, w, 0, w / 2], [0, 0, w, w, w / 2], [0, 0, 0, 0, w], [1, 1, 1, 1, 1]])

cube_coordinates = np.array([[0, w, w, 0, 0, 0, w, w],[0, 0, w, w, w, 0, 0, w],
        [0, 0, 0, 0, w, w, w, w],[1, 1, 1, 1, 1, 1, 1, 1],])


def drawLine(x, y, x2, y2):
    line = Line(Point(mid_x + x, mid_y - y), Point(mid_x + x2, mid_y - y2))
    line.setFill("black")
    line.draw(win)


def cube_draw(vertices):
    edges = [(i, i + 1) for i in range(7)] + [(0, 3), (0, 5), (6, 1), (7, 2), (7, 4)]
    for edge in edges:
        x1, y1 = vertices[edge[0]]
        x2, y2 = vertices[edge[1]]
        drawLine(x1, y1, x2, y2)


def Perspective_ABC(a, b, c):
    return np.array([[-c, 0, a, 0], [0, -c, b, 0], [0, 0, 0, 0], [0, 0, 1, -c]])


def Parallel_Projection(a, b, c):
    return np.array([[1, 0, -a / c, 0], [0, 1, -b / c, 0], [0, 0, 0, 0], [0, 0, 0, 1]])


def Oblique_Cavliar_Cabinet(f, Theta):
    Theta = np.radians(Theta)
    return np.array([[1, 0, f * np.cos(Theta), 0],[0, 1, f * np.sin(Theta), 0],
            [0, 0, 0, 0],[0, 0, 0, 1],] )


def matrixToVertices(matrix):
    return [[round(matrix[0][i] / matrix[3][i]), round(matrix[1][i] / matrix[3][i])]
        for i in range(len(matrix[0]))]


def pyramid_draw(vertices):
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4)]
    for edge in edges:
        x1, y1 = vertices[edge[0]]
        x2, y2 = vertices[edge[1]]
        drawLine(x1, y1, x2, y2)


def main_menu():
    draw_axes()
    while True:
        print("1. Perspective ")
        print("2. Parallel in the direction of v = aI + bJ + cK ")
        print("3. Oblique in terms of f and theta (b) Cavaliar (c) Cabinet ")
        print("Q. Quit")
        choice = input("Enter your choice: ").capitalize()
        if choice == "1":
            ch = input("press (a) CoP (0, 0, -d) : (b) CoP (a, b, c) ").capitalize()
            if ch == "A":
                output = Perspective_ABC(0, 0, -10) 
            elif ch == "B":
                output = Perspective_ABC(45, 55, 100) 
        elif choice == "2":
            output = Parallel_Projection(0, 0, 100)
        elif choice == "3":
            print("press 1 : for cavaliar  2: for cabinat ")
            choice1 = int(input("your choice -- "))
            if choice1 == 1:
                output = Oblique_Cavliar_Cabinet(1, 45)
            elif choice1 == 2:
                output = Oblique_Cavliar_Cabinet(1 / 2, 63.4)
        elif choice == "Q":
            break
        
        result = np.dot(output, cube_coordinates)
        Convert = matrixToVertices(result)
        cube_draw(Convert)

if __name__ == "__main__":
    main_menu()
    win.getMouse()
    win.close()
