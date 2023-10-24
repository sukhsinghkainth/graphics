########################################################################
# Assignment 1. Scan Conversion of Circle       
# Roll number: 22071293       
# Name: Sukhpreet Singh Kainth       
# Date: 7-09-2023       
########################################################################                      

import graphics as gr
import time
from math import *

win = gr.GraphWin("circle assignment", 1024, 728)
win.setBackground("black")
center_y = win.getHeight() / 2
center_x = win.getWidth() / 2


def draw_axes():
    x_axis = gr.Line(gr.Point(0, center_y), gr.Point(win.getWidth(), center_y))
    y_axis = gr.Line(gr.Point(center_x, 0), gr.Point(center_x, win.getHeight()))
    for axis in [x_axis, y_axis]:
        axis.setArrow("both")
        axis.setFill("yellow")
        axis.draw(win)


def PlotCirclePixel(h, k, x, y):
    win.plotPixel(h + x, k + y, "red")
    win.plotPixel(h + y, k + x, "CadetBlue")
    win.plotPixel(h - x, k + y, "aquamarine")
    win.plotPixel(h - y, k + x, "gold")
    win.plotPixel(h - x, k - y, "springGreen")
    win.plotPixel(h - y, k - x, "blueViolet")
    win.plotPixel(h + x, k - y, "purple")
    win.plotPixel(h + y, k - x, "Darkblue")


def direct_circle_draw(h, k, r):
    x, y = 0, r
    while x < y:
        x = x + 1
        y = sqrt(r * r - x * x)
        time.sleep(0.01)
        PlotCirclePixel(h, k, x, round(y))


def polar_domain_circle_draw(h, k, r):
    theta = 0
    theta_inc = 1 / r
    while theta <= pi / 4:
        x = r * cos(theta)
        y = r * sin(theta)
        theta = theta + theta_inc
        time.sleep(0.01)
        PlotCirclePixel(h, k, round(x), round(y))


def incremental_polar_domain(h, k, r):
    x, y = 0, r
    PlotCirclePixel(h, k, x, y)
    d_theta = 1 / r
    s = sin(d_theta)
    c = cos(d_theta)
    while x <= y:
        xTemp = x
        x = c * x - s * y
        y = s * xTemp + c * y
        PlotCirclePixel(h, k, round(x), round(y))


def Bresenham_circle(h, k, r):
    x, y = 0, r
    p = 3 - 2 * r
    PlotCirclePixel(h, k, x, y)
    while x <= y:
        if p <= 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x = x + 1
        PlotCirclePixel(h, k, x, y)


def MidPoint_Circle(h, k, r):
    x, y = 0, r
    p = 1 - r
    PlotCirclePixel(h, k, x, y)
    while x <= y:
        if p < 0:
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        PlotCirclePixel(h, k, x, y)


def main():
    while True:
        draw_axes()
        h = int(input("Enter value of h: "))  # value of h is 200
        k = int(input("Enter value of k: "))  # value of k is 200
        r = int(input("Enter value of r: "))  # value of r is 100
        print("\nDraw Circle on Screen Using points")
        #  For Right Handed Cartesian coordinate
        h = center_x + h
        k = center_y - k
        cir = gr.Circle(gr.Point(h, k), r)
        cir.setOutline("white")
        cir.draw(win)
        print("\nChoose an algorithm to plot the circle:")
        print("1. Plot Circle using Direct Algorithm")
        print("2. Plot Circle using Polar Algorithm")
        print("3. Plot Circle using Polar Increment Algorithm")
        print("4. Plot Circle using Bresenham Algorithm")
        print("5. Plot Circle using Mid-point Algorithm")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    direct_circle_draw(h, k, r)
                elif choice == 2:
                    polar_domain_circle_draw(h, k, r)
                elif choice == 3:
                    incremental_polar_domain(h, k, r)
                elif choice == 4:
                    Bresenham_circle(h, k, r)
                elif choice == 5:
                    MidPoint_Circle(h, k, r)
            else:
                print("Invalid input! Please choose a valid option (1-5).")
        except ValueError:
            print("Invalid input! Please enter a valid number (1-5).")

        ch = input("Do you wish to continue (Y/N)? ").lower()
        if ch != "y":
            break


if __name__ == "__main__":
    main()
