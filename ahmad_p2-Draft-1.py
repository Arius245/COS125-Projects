# File: ahmad_p2.py 
# Author: Arius Ahmad 
# Date: 11/18/22 
# Section: 1003 
# E-mail: arius.ahmad@maine.edu  
# Collaboration: I worked with McKade Wing (mckade.wing@maine.edu)

from graphics import *
import random

# def ColorRect(rect, r):
#     if r < 0.15:
#         rect.setFill("blue")
#     elif r < 0.25:
#         rect.setFill("red")
#     elif r < 0.9:
#         rect.setFill("yellow")
#     else:
#         rect.setFill("white")
    

def SplitVert(win,w,a):
    #     aLine = graphics.Line(graphics.Point(0,a),graphics.Point(w,a))
    #     bLine = graphics.Line(graphics.Point(b,0),graphics.Point(b,h))

    tempRect = Rectangle(Point(0,0),Point(w,a))
    
    # tempRect.setFill("red")
    # ColorRect(tempRect,w)
    r = random.random()
    if r < 0.15:
        tempRect.setFill("blue")
    elif r < 0.25:
        tempRect.setFill("red")
    elif r < 0.9:
        tempRect.setFill("yellow")
    else:
        tempRect.setFill("white")

    tempRect.setOutline("black")
    tempRect.draw(win)

def SplitHori(win,h,b):
    tempRect2 = Rectangle(Point(0,0),Point(b,h))
    
    # tempRect2.setFill("green")
    # ColorRect(tempRect2,h)
    r = random.random()
    if r < 0.15:
        tempRect2.setFill("blue")
    elif r < 0.25:
        tempRect2.setFill("red")
    elif r < 0.9:
        tempRect2.setFill("yellow")
    else:
        tempRect2.setFill("white")

    tempRect2.setOutline("black")
    tempRect2.draw(win)

def SplitBoth(win,w,h,a,b):
        
        # tempRect = graphics.Rectangle(graphics.Point(0,0),graphics.Point(w,a))
        # # tempRect.setFill("red")
        # ColorRect(tempRect)
        # tempRect.setOutline("black")
        # tempRect2 = graphics.Rectangle(graphics.Point(0,0),graphics.Point(b,h))
        # # tempRect2.setFill("green")
        # ColorRect(tempRect2)
        # tempRect2.setOutline("black")
        
        # # aRect.setOutline("black")
        # # aRect.draw(win)
        
        # # aLine.draw(win)
        # # bLine.draw(win)

        # tempRect.draw(win)
        # tempRect2.draw(win)

    SplitVert(win,w,a)
    SplitHori(win,h,b)


def main():
    win = GraphWin("My Drawing", 600, 600)
    w = random.randint(0,600)
    h = random.randint(0,600)
    # newW = w//2
    # newH = h//2
    a = random.uniform(w*0.31,w*0.68)
    b = random.uniform(h*0.31,h*0.68)
    rect1 = Rectangle(Point(0,0), Point(w, h))
    
    # rect1.setFill("purple")
    # ColorRect(rect1,w)
    r = random.random()
    if r < 0.15:
        rect1.setFill("blue")
    elif r < 0.25:
        rect1.setFill("red")
    elif r < 0.9:
        rect1.setFill("yellow")
    else:
        rect1.setFill("white")
    
    rect1.setOutline("black")
    rect1.draw(win)

    newW = float(w) * 1.5
    ranInt = int(random.uniform(90,newW))
    ranNum = random.randrange(0,3)
    if ranInt < w:
        if ranNum == 0:
            SplitBoth(win,w,h,a,b)
        elif ranNum == 1:
            SplitVert(win,w,a)
        elif ranNum == 2:
            SplitHori(win,h,b)
    
    # if w >= 300 and h >= 300:
    #     SplitBoth(win,w,h,a,b)
    # elif w >= 300:
    #     SplitVert(win,w,a)
    # elif h >= 300:
    #     SplitHori(win,h,b)  
    # else:
    #     rect1.setOutline("black")
    #     rect1.draw(win)
    
    win.getMouse()
    win.close()
main()
