from graphics import *
import numpy as np

win = GraphWin("graphics", 1200, 600)
win.setBackground("black")
center_y = win.getHeight() / 2
center_x = win.getWidth() / 2

def drawSTar():
    l1 = Line(Point(50, 50), Point(100, 150))
    l2 = Line(Point(100, 150), Point(150, 50))
    l3 = Line(Point(150, 50), Point(50, 100))
    l4 = Line(Point(50, 100), Point(150, 100))
    l5 = Line(Point(150, 100), Point(50, 50))
    for l in l1, l2, l3, l4, l5:
        l.setOutline("white") 
        l.draw(win)

drawSTar()

t1 =Text(Point(center_x,center_y),"CG SUCks (❁´◡`❁)😭🤡")
t1.setTextColor("white")
t1.setSize(20)
t1.draw(win)

def drawline(x1, y1, x2, y2):
    l1 = Line(Point(x1, y1), Point(x1, y2))
    l2 = Line(Point(x2, y1), Point(x2, y2))
    l3 = Line(Point(x1, y1), Point(x2, y1))
    l4 = Line(Point(x1, y2), Point(x2, y2))
    for l in l1, l2, l3, l4:
        l.setOutline("white") 
        l.draw(win)


def translation(tx, ty):
    tranlation_matrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    return tranlation_matrix


def scaling(sx, sy, h, k):
    scaling_m = np.array([[sx, 0, h * (1 - sx)], [0, sy, k * (1 - sy)], [0, 0, 1]])
    return scaling_m

def reflection(xis):
    if xis == "X":
        x = 1 
        y = -1
    else:
        x = -1 
        y = 1
    
    rf_m = np.array([[x,0,0],[0,y,0],[0,0,1]])
    return rf_m

def rotation(angle, h, k):
    theta = np.radians(angle)
    r_m = np.array(
        [[np.cos(theta),   -np.sin(theta),  h * (1 - np.cos(theta)) + k * np.sin(theta),],
        [np.sin(theta), np.cos(theta), k * (1 - np.cos(theta)) - h * np.sin(theta)],
        [0, 0, 1]]
    )
    return r_m


x1, y1, x2, y2 = 50, 50, 100, 150 
drawline(x1 + center_x, center_y - y1, center_x + x2, center_y - y2)

homo_matrix = np.array([[x1, y1, 1], [x2, y2, 1]]).T
# result = translation(-250, -200)
# result = scaling(1.25, 0.75, 50, 50)
# result = rotation(45, 125, 100)
x = "X"
result = reflection(x)
output = np.dot(result, homo_matrix)

x1_new, y1_new, _ = output[:, 0]
x2_new, y2_new, _ = output[:, 1] 

drawline(center_x + x1_new, center_y - y1_new, center_x + x2_new, center_y - y2_new)
win.getMouse()
win.close()
