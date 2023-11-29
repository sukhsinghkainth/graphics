########################################################################
# Assignment 7: Projection
# Roll number: 22071211, 22071293
# Name: Bhavya, Sukhpreet Singh Kainth
# Date: 13-10-2023
########################################################################

import graphics as gr
import numpy as np

max_x = 1200
max_y=700
mid_x=max_x/2
mid_y=max_y/2

def create_Window(color):  
    win = gr.GraphWin("my window", max_x, max_y) #creating window object
    win.setBackground(color)
    lines(mid_x, mid_y, max_x, mid_y, "white", win) # x-axis
    lines(mid_x, 0, mid_x, mid_y, "white", win) # y-axis
    lines(0, max_y, mid_x, mid_y, "white", win) # y-axis
    return win

def close_Window(win): #closing window
    win.getMouse()
    win.close()

def lines(x1, y1, x2, y2, color, win): # for drawing lines
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2))
    line.setFill(color)
    line.draw(win)
    
def matrixToVertices( n, matrix):
    new_vertices=[]
    for i in range(n):
        new_vertices.append([round(matrix[0][i] / matrix[3][i]), round(matrix[1][i] / matrix[3][i])])
    return new_vertices

def perspective(a, b, c):
    perspective_matrics = np.array([[-c, 0, a, 0],
                                    [0, -c, b, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 1, -c]])
    return perspective_matrics

def parallel(a, b, c):
    parallel_marics = np.array([[1, 0, -a/c, 0],
                                [0, 1, -b/c, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 1]])
    return parallel_marics

def oblique(f, theta):
    theta = np.radians(theta)
    oblique = np.array([[1, 0, f * np.cos(theta), 0],
                        [0, 1, f * np.sin(theta), 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 1]])
    return oblique

def drawLine( x1, y1, x2, y2, win):
    line = gr.Line(gr.Point(mid_x + x1, mid_y - y1), gr.Point(mid_x + x2, mid_y - y2))
    line.setFill("white")
    line.draw(win)

def drawCube(vertices, win):
    for i in range(7):
        x1 = vertices[i][0]
        y1= vertices[i][1]
        x2 = vertices[i+1][0]
        y2 = vertices[i+1][1]
        drawLine(x1, y1, x2, y2, win)
    drawLine(vertices[0][0], vertices[0][1], vertices[3][0], vertices[3][1], win)
    drawLine(vertices[0][0], vertices[0][1], vertices[5][0], vertices[5][1], win)
    drawLine(vertices[6][0], vertices[6][1], vertices[1][0], vertices[1][1], win)
    drawLine(vertices[7][0], vertices[7][1], vertices[2][0], vertices[2][1], win)
    drawLine(vertices[7][0], vertices[7][1], vertices[4][0], vertices[4][1], win)

def drawPyramid(vertices, win):
    m_x = vertices[4][0]
    m_y = vertices[4][1]
    for i in range(4):
        x1 =  vertices[i][0]
        y1 =  vertices[i][1]
        x2 = vertices[i+1][0]
        y2 = vertices[i+1][1]
        drawLine(x1, y1, x2, y2, win)
        drawLine(x1, y1, m_x, m_y, win)
        
def main():
    w = 100
    cube = np.array([[0, w, w, 0, 0, 0, w, w],
                    [0, 0, w, w, w, 0, 0, w],
                    [0, 0, 0, 0, w, w, w, w],
                    [1, 1, 1, 1, 1, 1, 1, 1]])
    pyramid = np.array([[0, w, w, 0, w/2],
                        [0, 0, w, w, w/2],
                        [0, 0, 0, 0, w],
                        [1, 1, 1, 1, 1]])
    object_ch = int(input("1 for cube \n 2 for pyramid \nenter: "))
    if(object_ch == 1):
        object = cube
        n = 8
    else:
        object = pyramid
        n = 5
    while(True):
        print('''1. Perspective with CoP (0, 0, -d) 
2. Perspective with CoP (a, b, c)
3. Parallel in the direction of v = aI + bJ + cK
4. Oblique in terms of f and general
5. Oblique in terms of f and theta Cavaliar 
6. Oblique in terms of f and theta cabinet
7. EXIT''')
        choice = int(input('Enter choice:'))
        
        if(choice==7):
            break
        match(choice):
            case 1:
                d = int(input("enter the value for d: "))
                win = create_Window("black")
                projection_matrix = perspective(0, 0, -d)
            case 2:
                a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
                win = create_Window("black")
                projection_matrix = perspective(a, b, c)
            case 3:
                win = create_Window("black")
                projection_matrix = parallel(0, 0, 100)
            case 4:
                f = int(input("enter the vakue of f: "))
                theta = int(input("enter the vakue of theta: "))
                win = create_Window("black")
                projection_matrix = oblique(f, theta)
            case 5:
                win = create_Window("black")
                projection_matrix = oblique(1, 45)
            case 6:
                win = create_Window("black")
                projection_matrix = oblique(1/2, 63.4)
            case _:
                print("enter right choice")
                continue
        result = np.dot(projection_matrix, object)
        vertices = matrixToVertices(5, result)
        if object_ch == 1 :
            drawCube(vertices, win)
        elif object_ch == 2:
            drawPyramid(vertices, win)
        close_Window(win)
if __name__ == "__main__":
    main()
