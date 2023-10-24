########################################################################
# Assignment 4: 2D Transformations
# Roll number: 22071293
# Name: Sukhpreet Singh Kainth
# Date: 13-10-2023  
########################################################################

from graphics import *
import numpy as np

win = GraphWin("2D Transformations", 1200, 780)
center_x = win.getWidth() / 2
center_y = win.getHeight() / 2
h = 90
k = 65
Polygon_points = [(25, 35), (160, 50), (35, 125), (100, -5), (135, 135)]
Homogeneous_Matrix = np.array([[x, y, 1] for x, y in Polygon_points]).T


def draw_axes():
    x_axis = Line(Point(0, center_y), Point(win.getWidth(), center_y))
    y_axis = Line(Point(center_x, 0), Point(center_x, win.getHeight()))
    for axis in [x_axis, y_axis]:
        axis.setArrow("both")
        axis.setFill("black")
        axis.draw(win)


def translation(tx, ty):
    translation_matrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    return np.dot(translation_matrix, Homogeneous_Matrix)


def scaling(sx, sy, h, k):
    scaling_matrix = np.array([[sx, 0, h * (1 - sx)], [0, sy, k * (1 - sy)], [0, 0, 1]])
    return np.dot(scaling_matrix, Homogeneous_Matrix)


def rotation(angle, h, k):
    Theta = np.radians(angle)
    rotation_matrix = np.array([ [np.cos(Theta), -np.sin(Theta), -h * np.cos(Theta) + k * np.sin(Theta) + h],
            [np.sin(Theta), np.cos(Theta), -h * np.sin(Theta) - k * (np.cos(Theta) + k),],
             [0, 0, 1]])
    return np.dot(rotation_matrix, Homogeneous_Matrix)


def rotation_origin(angle):
    Theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(Theta), -np.sin(Theta), 0],
            [np.sin(Theta), np.cos(Theta), 0],
            [0, 0, 1]])
    return np.dot(rotation_matrix, Homogeneous_Matrix)

def scaling_origin(sx, sy):
    scaling_origin_matrix = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    return np.dot(scaling_origin_matrix, Homogeneous_Matrix)


def reflection_y_equals_x():
    reflection_matrix = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    return np.dot(reflection_matrix, Homogeneous_Matrix)


def reflection_y_equals_neg_x():
    reflection_matrix = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])
    return np.dot(reflection_matrix, Homogeneous_Matrix)


def reflection_general_axis(x1, y1, x2, y2):
    l1 = Line(Point(x1 + center_x, center_y - y1), Point(center_x + x2, center_y - y2))
    l1.setFill("green")
    l1.draw(win)
    if x1 == x2:
        reflection_matrix = np.array([[-1, 0, 2 * x1], [0, 1, 0], [0, 0, 1]])
    else:
        m = (y2 - y1) / (x2 - x1)
        m2 = m * m
        b = y1 - m * x1
        reflection_matrix = np.array( [ [(1 - m2) / (1 + m2), (2 * m) / (1 + m2), -(2 * b * m) / (1 + m2)],
                [(2 * m) / (1 + m2), -(1 - m2) / (1 + m2), (2 * b) / (1 + m2)],
                [0, 0, 1],])
    return np.dot(reflection_matrix, Homogeneous_Matrix)


def reflection_about_xis(xis):
    if xis == "x":
        x, y = 1, -1
    else:
        x, y = -1, 1
    refl_matrix = np.array([[x, 0, 0], [0, y, 0], [0, 0, 1]])
    return np.dot(refl_matrix, Homogeneous_Matrix)


def shearing(a, b):
    trans = np.array([[1, a, 0], [b, 1, 0], [0, 0, 1]])
    return np.dot(trans, Homogeneous_Matrix)


def shearing_y(a):
    trans = np.array([[1, a, 0], [0, 1, 0], [0, 0, 1]])
    return np.dot(trans, Homogeneous_Matrix)


def shearing_x(b):
    trans = np.array([[1, 0, 0], [b, 1, 0], [0, 0, 1]])
    return np.dot(trans, Homogeneous_Matrix)


polygon = Polygon([Point(x + center_x, center_y - y) for x, y in Polygon_points])
polygon.setOutline("blue")
polygon.draw(win)


def main():
    draw_axes()
    transformed_polygon = Polygon(
        [Point(x + center_x, center_y - y) for x, y in Polygon_points]
    )
    transformed_polygon.setFill("red")
    transformed_polygon.draw(win)

    while True:
        print(
            """Enter '1' for translation
Enter '2' for scaling about origin
Enter '3' for rotation
Enter '4' for reflection about x-axis or y-axis
Enter '5' for reflection about y = x
Enter '6' for reflection about y = -x
Enter '7' for reflection about a general axis
Enter '8' for scaling about a given point
Enter '9' for rotation about a given point
Enter '10' for shearing
Enter '11' for shearing x 
Enter '12' for shearing y 
Enter 'Q' to quit"""
        )
        print("----------------")
        choice = input("Enter your choice: ").capitalize()

        if choice == "1":
            tx = int(input("Enter translation in the X direction: "))
            ty = int(input("Enter translation in the Y direction: "))
            Homogeneous_Matrix = translation(tx, ty)
        elif choice == "2":
            sx = float(input("Enter scaling factor for X: "))
            sy = float(input("Enter scaling factor for Y: "))
            Homogeneous_Matrix = scaling_origin(sx, sy)
        elif choice == "3":
            angle = int(input("Enter rotation angle (in degrees): "))
            Homogeneous_Matrix = rotation_origin(angle)
        elif choice == "4":
            xis = input(
                "Enter 'x' for reflection about x-axis, or 'y' for reflection about y-axis: "
            ).lower()
            Homogeneous_Matrix = reflection_about_xis(xis)
        elif choice == "5":
            Homogeneous_Matrix = reflection_y_equals_x()
        elif choice == "6":
            Homogeneous_Matrix = reflection_y_equals_neg_x()
        elif choice == "7":
            x1 = int(input("Enter x1 for the axis: "))
            y1 = int(input("Enter y1 for the axis: "))
            x2 = int(input("Enter x2 for the axis: "))
            y2 = int(input("Enter y2 for the axis: "))
            Homogeneous_Matrix = reflection_general_axis(x1, y1, x2, y2)
        elif choice == "8":
            sx = float(input("Enter scaling factor for sX: "))
            sy = float(input("Enter scaling factor for sY: "))
            h = int(input("Enter X coordinate of the point h: "))
            k = int(input("Enter Y coordinate of the point k: "))
            Homogeneous_Matrix = scaling(sx, sy, h, k)
        elif choice == "9":
            angle = int(input("Enter rotation angle (in degrees): "))
            h = int(input("Enter X coordinate of the pivot point: "))
            k = int(input("Enter Y coordinate of the pivot point: "))
            Homogeneous_Matrix = rotation(angle, h, k)
        elif choice == "10":
            a = float(input("Enter shearing a parameter: "))
            b = float(input("Enter shearing b parameter: "))
            Homogeneous_Matrix = shearing(a, b)
        elif choice == "11":
            a = float(input("Enter shearing_x a parameter: "))
            Homogeneous_Matrix = shearing_x(a)
        elif choice == "12":
            b = float(input("Enter shearing_y b parameter: "))
            Homogeneous_Matrix = shearing_y(b)
        elif choice == "Q":
            break

        transformed_vertices = [ Point(int(x) + center_x, center_y - int(y))
            for x, y, _ in Homogeneous_Matrix.T]
        transformed_polygon.undraw()
        transformed_polygon = Polygon(transformed_vertices)
        transformed_polygon.setOutline("black")
        transformed_polygon.draw(win)

    win.close()


if __name__ == "__main__":
    main()
