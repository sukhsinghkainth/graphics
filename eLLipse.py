########################################################################
# Assignment 3. Scan Conversion of Ellipse
# Roll number: 22071293
# Name: Sukhpreet Singh Kainth
# Date: 14-09-2023
########################################################################

import graphics as gr
from math import *
import time

win = gr.GraphWin("Scan Converting Ellipse assignment", 1240, 1000)
win.setBackground("black")
center_y = win.getHeight() / 2
center_x = win.getWidth() / 2


def draw_axes():
    x_axis = gr.Line(gr.Point(0, center_y), gr.Point(win.getWidth(), center_y))
    y_axis = gr.Line(gr.Point(center_x, 0), gr.Point(center_x, win.getHeight()))
    for axis in [x_axis, y_axis]:
        axis.setArrow("both")
        axis.setFill("white")
        axis.draw(win)


def Put_Ellipse_Pixel(h, k, x, y):
    win.plotPixel(h + x, k + y, "darkblue")
    win.plotPixel(h - x, k + y, "aquamarine")
    win.plotPixel(h - x, k - y, "purple")
    win.plotPixel(h + x, k - y, "gold")


def Direct_Ellipse_Draw(h, k, a, b):
    x, y = 0, b
    Put_Ellipse_Pixel(h, k, x, y)
    b_sqr, a_sqr = b * b, a * a
    while b_sqr * x <= a_sqr * y:
        x = x + 1
        y = b * sqrt(1 - (x * x) / (a_sqr))
        Put_Ellipse_Pixel(h, k, x, round(y))
        time.sleep(0.01)
    y = round(y)
    while y > 0:
        y = y - 1
        x = a * sqrt(1 - (y * y) / (b_sqr))
        Put_Ellipse_Pixel(h, k, round(x), y)
        time.sleep(0.01)


def Polar_Domain_Ellipse_draw(h, k, a, b):
    if a > b:
        dTHeta = 1 / a
    else:
        dTHeta = 1 / b
    Theta = 0
    x, y = a, 0
    Put_Ellipse_Pixel(h, k, x, y)
    pi_by_2 = pi / 2
    while Theta <= pi_by_2:
        Theta = Theta + dTHeta
        x = a * cos(Theta)
        y = b * sin(Theta)
        Put_Ellipse_Pixel(h, k, round(x), round(y))
        time.sleep(0.01)


def Incremental_Polar_Domain_Ellipse(h, k, a, b):
    if a > b:
        dTheta = 1 / a
    else:
        dTheta = 1 / b
    c = cos(dTheta)
    sab = (a / b) * sin(dTheta)
    sba = (b / a) * sin(dTheta)
    x, y = a, 0
    Put_Ellipse_Pixel(h, k, x, y)
    while x >= 0:
        xTemp = x
        x = x * c - sab * y
        y = xTemp * sba + y * c
        Put_Ellipse_Pixel(h, k, x, round(y))
        time.sleep(0.01)


def Mid_Point_Ellipse(h, k, a, b):
    x, y = 0, b
    b_sqr, a_sqr = b * b, a * a
    p = (b_sqr) - (a_sqr * b) + ((a_sqr) / 4)
    p = round(p)
    Put_Ellipse_Pixel(h, k, x, y)
    while b_sqr * x <= a_sqr * y:
        if p < 0:
            p = p + b_sqr * (2 * x + 3)
        else:
            p = p + (b_sqr) * (2 * x + 3) + (a_sqr) * (-2 * y + 2)
            y = y - 1
        x += 1
        Put_Ellipse_Pixel(h, k, x, y)
        time.sleep(0.01)
    p = b_sqr * (x + 0.5) * (x + 0.5) + (a_sqr) * (y - 1) * (y - 1) - a_sqr * b_sqr
    p = round(p)
    while y > 0:
        if p < 0:
            p = p + (b_sqr) * (2 * x + 2) + (a_sqr) * (-2 * y + 3)
            x = x + 1
        else:
            p = p + (a_sqr) * (-2 * y + 3)
        y -= 1
        Put_Ellipse_Pixel(h, k, x, y)
        time.sleep(0.01)


def main():
    while True:
        draw_axes()
        h = int(input("Enter value of h: "))
        k = int(input("Enter value of k: "))
        a = 100
        b = 50
        print("\nDraw Ellipse on Screen Using points")
        #  For Right Handed Cartesian coordinate
        h = center_x + h
        k = center_y - k
        Ellipis = gr.Oval(gr.Point(h - a, k - b), gr.Point(h + a, k + b))
        Ellipis.setOutline("white")
        Ellipis.draw(win)
        print("\nChoose an algorithm to plot the Ellipse:")
        print("1. Plot Ellipse using Direct Algorithm")
        print("2. Plot Ellipse using Mid-Point Algorithm")
        print("3. Plot Ellipse using Polar Domain Algorithm")
        print("4. Plot Ellipse using Incremental Polar Domain Algorithm")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    Direct_Ellipse_Draw(h, k, a, b)
                elif choice == 2:
                    Mid_Point_Ellipse(h, k, a, b)
                elif choice == 3:
                    Polar_Domain_Ellipse_draw(h, k, a, b)
                elif choice == 4:
                    Incremental_Polar_Domain_Ellipse(h, k, a, b)
            else:
                print(" Please choose a valid option (1-5) ")
        except ValueError:
            print(" Enter a valid number 1-5 ")

        ch = input("Do you wish to continue Y / N ").lower()
        if ch != "y":
            break


if __name__ == "__main__":
    main()
