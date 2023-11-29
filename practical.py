########################################################################
# Assignment 5: 2D Transformations
# Roll number: 22071211
# Name: Bhavya
# Date: 13-10-2023
########################################################################

import graphics as gr
import numpy as np
import math
def create_Window(max_x, max_y, color):  
    win = gr.GraphWin("my window", max_x, max_y) #creating window object
    win.setBackground(color)
    lines(0, max_y/2, max_x, max_y/2, "white", win) # x-axis
    lines(max_x/2, 0, max_x/2, max_y, "white", win) # y-axis
    return win

def close_Window(win): #closing window
    win.getMouse()
    win.close()

def lines(x1, y1, x2, y2, color, win): # for drawing lines
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2))
    line.setFill(color)
    line.setArrow("both")
    line.draw(win)

def draw_polygon(polygon, vertices, color, win):
    polygon.undraw()
    polygon = gr.Polygon(vertices)
    polygon.setFill(color)
    polygon.setOutline("white")
    polygon.draw(win)
    return polygon

def matrixToVertices( n, mid_x, mid_y, matrix):
    new_vertices=[]
    for i in range(n):
        new_vertices.append(round(matrix[0][i]) )
        new_vertices.append(round(matrix[1][i]) )
    return new_vertices   
 
def translate(tx, ty, point_matrix):
    translation_matrix = np.array([[1,0,tx],
                                  [0,1,ty],
                                  [0,0,1]])
    return np.dot(translation_matrix, point_matrix)

def scaling(sx, sy, h, k, point_matrix):
    scaling_matrix = np.array([[sx,0,h*(1-sx)],
                              [0,sy,k*(1-sy)],
                              [0,0,1]])
    return np.dot(scaling_matrix, point_matrix)

def rotation(theta, h, k, point_matrix):
    theta = np.radians(theta)
    rotation_matrix = np.array([[math.cos(theta), -math.sin(theta), -h*math.cos(theta) + k*math.sin(theta) + h],
                               [math.sin(theta), math.cos(theta), -h*math.sin(theta)- k* math.cos(theta) + k],
                               [0,0,1]])
    return np.dot(rotation_matrix, point_matrix)

def mirrorReflectionAboutAxis(choice, point_matrix):
    if choice=='x':
        mx, my = 1, -1
    elif choice=='y':
        mx, my = -1, 1
    ml_matrix = np.array([[mx, 0, 0], 
                         [0, my, 0],
                         [0, 0, 1]])
    return np.dot(ml_matrix, point_matrix)

def mirrorReflectionAboutXY(x1, y1, x2, y2, point_matrix, win):
    lines(x1, y1, x2, y2, "white", win)
    if(x1==x2): # special case when x1 and x2 are equal or with horixontal line
        ml_matrix= np.array([[-1, 0, 2*x1],
                             [0, 1, 0],
                             [0, 0, 1]])
        return np.dot(ml_matrix, point_matrix)
    m=(y2-y1)/(x2-x1)
    b= y1 - m*x1
    m_sqr=m*m
    ml_matrix = np.array([[(1-m_sqr)/(1+m_sqr), (2*m)/(1+m_sqr), -(2*m)/(1+m_sqr)],
                          [(2*m)/(1+m_sqr), -(1-m_sqr)/(1+m_sqr), (2*b)/(1+m_sqr)],
                          [0, 0, 1]])
    return np.dot(ml_matrix, point_matrix)

def shearing(a, b, point_matrix):
    sh_matrix = np.array([[1, a, 0],
                          [b, 1, 0],
                          [0, 0, 1]])
    return np.dot(sh_matrix, point_matrix)

def main():
    max_x = 780
    max_y=480
    mid_x=max_x/2
    mid_y=max_y/2
    n=5
    win = create_Window(max_x, max_y, "black")
    vertices_matrix=np.array([ [25, 160, 35, 100, 135],
                              [35, 50, 125, -5, 135],
                              [1, 1, 1, 1, 1] ])
    vertices = matrixToVertices(n, mid_x, mid_y, vertices_matrix)
    polygon = gr.Polygon(vertices)
    polygon.setOutline("white")
    polygon.draw(win)
    
    while(True):
        print("""   1. translation.
    2. Scaling about origin
    3. scaling about point(h,k)
    4. Rotation about origin
    5. Rotation about point(h,k)
    6. Mirror reflection about axis ( x or y )
    7. Mirror reflection about line (x1, y1) to (x2, y2)
    8. Shearing about x-axis
    9. Shearing about y-axis
    10. Shearing about origin
    11. EXIT""")
        choice = int(input("enter choice:-"))
        if choice == 11:
            break
        match(choice):
            case 1: #translation
                tx=int(input("enter value for tx= "))
                ty=int(input("enter value for ty= "))
                result = translate(tx, ty, vertices_matrix)
                color="red"
            case 2:     # scaling about origin
                sx=int(input("enter value for sx= "))
                sy=int(input("enter value for sy= "))
                result = scaling(sx, sy, 0, 0, vertices_matrix)
                color="pink"
            case 3: #scaling about point
                sx=int(input("enter value for sx= "))
                sy=int(input("enter value for sy= "))
                h=int(input("enter value for h= "))
                k=int(input("enter value for k= "))
                result = scaling(sx, sy, h, k, vertices_matrix)
                color= "green"
            case 4: # rotation about origin
                theta=int(input("enter value for theta= "))
                result = rotation(theta, 0, 0, vertices_matrix)
                color="blue"
            case 5: # rotation about point
                theta=int(input("enter value for theta= "))
                h=int(input("enter value for h= "))
                k=int(input("enter value for k= "))
                result = rotation(theta, h, k, vertices_matrix)
                color="grey"
            case 6:   #reflection about axis
                axis = input("press x for x-axis \npress y for y-axis:")
                result = mirrorReflectionAboutAxis(axis, vertices_matrix)
                color="skyblue"
            case 7: # reflection using points
                x1 = int(input("enter the value of x1: "))
                y1 = int(input("enter the value of y1: "))
                x2 = int(input("enter the value of x2: "))
                y2 = int(input("enter the value of y2: "))
                result = mirrorReflectionAboutXY(x1, y1, x2, y2, vertices_matrix, win)
                color="yellow"
            case 8: #shearing about x axis
                b = int(input("Enter the value of b: "))
                result = shearing(0, b, vertices_matrix)
                color="cyan"
            case 9: #shearing about y axis
                a = int(input("Enter the value of a: "))
                result = shearing(a, 0, vertices_matrix)
                color= "gold"
            case 10: #shearing about origin
                a = int(input("Enter the value of a: "))
                b = int(input("Enter the value of b: "))
                result = shearing(a, b, vertices_matrix)
                color="brown"
        new_vertices = matrixToVertices(n, mid_x, mid_y, result)
        polygon = draw_polygon(polygon, new_vertices, color, win)
                  
    close_Window(win)
if __name__ == "__main__":
    main()