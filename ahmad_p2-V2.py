# File: ahmad_p2.py 
# Author: Arius Ahmad 
# Date: 11/18/22 
# Section: 1003 
# E-mail: arius.ahmad@maine.edu  
# Collaboration: I worked with McKade Wing (mckade.wing@maine.edu)

from graphics import *
import random

w = 700
h = 700

def getW(rect):
    point2 = rect.getP2()
    point1 = rect.getP1()
    point2X = point2.getX()
    point1X = point1.getX()
    p2x = point2X - point1X
    p1x = point1X 

    return p2x, p1x

def getH(rect):
    point2 = rect.getP2()
    point1 = rect.getP1()
    point2Y = point2.getY()
    point1Y = point1.getY()
    p2y = point2Y - point1Y
    p1y = point1Y 

    return p2y, p1y

def ColorSet(rect):
    r = random.random()
    if r < 0.09:
        rect.setFill("yellow")
    elif r < 0.15:
        rect.setFill("blue")
    elif r < 0.25:
        rect.setFill("red")
    else:
        rect.setFill("white")

def deterSplit(win,rect):
        # Recursive Case 1
        p2x, p1x = getW(rect)
        p2y, p1y = getH(rect)

        if p2x > (w / 2) or p2y > (h / 2):
            if p2x > (w / 2) and p2y > (h / 2):
                SplitBoth(win,rect)
            elif p2x > (w / 2):
                vertRect , vertRect2 = SplitVert(win,rect)
                deterSplit(win,vertRect)
                deterSplit(win,vertRect2)
            elif p2y > (h / 2):
                horiRect , horiRect2 = SplitHori(win,rect)
                deterSplit(win,horiRect)
                deterSplit(win,horiRect2)
        
        # Recursive Case 2
        # elif p2x < (w / 2) and p2x > 90 or p2y < (h / 2) and p2y > 90:
        #     ranNum = random.random()
        #     if ranNum >= 0.5:
        #         if (p2x < (w / 2) and p2x > 90) and (p2y < (h / 2) and p2y > 90):
        #             SplitBoth(win,rect, p2x, p2y, p1x, p1y)
        #         elif p2x < (w / 2) and p2x > 90:
        #             SplitVert(win,rect, p2x, p2y, p1x, p1y)
        #         elif p2y < (h / 2) and p2y > 90:
        #             SplitHori(win,rect, p2x, p2y, p1x, p1y)

        # Base Case
        else:
            return

# def SplitBoth(win,rect, p2x, p2y, p1x, p1y):
def SplitBoth(win,rect):

    p2x, p1x = getW(rect)
    p2y, p1y = getH(rect)
    
    a = random.uniform((p2x*0.31),(p2x*0.68))
    # print("a:", a)
    b = random.uniform((p2y*0.31),(p2y*0.68))
    # print("b:", b)

    # Split Both Ways
    if p2x > (w / 2) and p2y > (h / 2):
        tempRect = Rectangle(Point(p1x,p1y),Point(a,b))
        # ColorSet(tempRect)
        # tempRect.setFill("red")
        tempRect.setOutline("black")
        tempRect.draw(win)

        tempRect2 = Rectangle(Point(p1x,b),Point(a,p2y))
        # ColorSet(tempRect2)
        # tempRect2.setFill("red")
        tempRect2.setOutline("black")
        tempRect2.draw(win)

        tempRect3 = Rectangle(Point(a,p1y),Point(p2x,b))
        # ColorSet(tempRect3)
        # tempRect3.setFill("red")
        tempRect3.setOutline("black")
        tempRect3.draw(win)

        tempRect4 = Rectangle(Point(a,b),Point(p2x,p2y))
        # ColorSet(tempRect4)
        # tempRect4.setFill("red")
        tempRect4.setOutline("black")
        tempRect4.draw(win)
            
        print("BOTH")
        print(tempRect)
        print(tempRect2)
        print(tempRect3)
        print(tempRect4)
        print()

        deterSplit(win,tempRect)
        deterSplit(win,tempRect2)
        # deterSplit(win,tempRect3)
        # deterSplit(win,tempRect4)


        # vertRect, vertRect2 = SplitVert(win,rect)

        # horiRect , horiRect2 = SplitHori(win,vertRect)
        # horiRect3 , horiRect4 = SplitHori(win,vertRect2)
            
        # deterSplit(win,horiRect)
        # deterSplit(win,horiRect2)
        # deterSplit(win,horiRect3)
        # deterSplit(win,horiRect4)

def SplitVert(win,rect):
    p2x, p1x = getW(rect)
    p2y, p1y = getH(rect)

    a = random.uniform((p2x*0.31),(p2x*0.68))
    # print("a:", a)
    b = random.uniform((p2y*0.31),(p2y*0.68))
    # print("b:", b)

    if p2x > (w / 2):
        vertRect = Rectangle(Point(p1x,p1y),Point(a,p2y))
        vertRect2 = Rectangle(Point(a,p1y),Point(p2x,p2y))
        # ColorSet(vertRect)
        # vertRect.setFill("blue")
        # vertRect.setOutline("black")
        vertRect.setOutline("blue")
        vertRect.draw(win)
            
        print("VERT")
        print(vertRect)
        print()
            
        deterSplit(win,vertRect)
        deterSplit(win,vertRect2)

        return vertRect , vertRect2
        
def SplitHori(win,rect):
    p2x, p1x = getW(rect)
    p2y, p1y = getH(rect)

    a = random.uniform((p2x*0.31),(p2x*0.68))
    # print("a:", a)
    b = random.uniform((p2y*0.31),(p2y*0.68))
    # print("b:", b)

    if p2y > (h / 2):
        horiRect = Rectangle(Point(p1x,p1y),Point(p2x,b))
        horiRect2 = Rectangle(Point(p1x,b),Point(p2x,p2y))
        # ColorSet(horiRect)
        # horiRect.setFill("yellow")
        # horiRect.setOutline("black")
        horiRect.setOutline("red")
        horiRect.draw(win)
            
        print("HORI")
        print(horiRect)
        print()
            
        deterSplit(win,horiRect)
        deterSplit(win,horiRect2)

        return horiRect , horiRect2
            

def main():
    win = GraphWin("My Drawing", w, h)
    
    rect1 = Rectangle(Point(0,0), Point(w, h))
    # ColorSet(rect1)     
    rect1.setOutline("black")
    # rect1.draw(win)

    deterSplit(win,rect1)
    
    win.getMouse()
    win.close()
main()