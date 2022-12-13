# File: ahmad_p2_XC.py 
# Author: Arius Ahmad 
# Date: 11/18/22 
# Section: 1003 
# E-mail: arius.ahmad@maine.edu  
# Collaboration: I worked with McKade Wing (mckade.wing@maine.edu) and Gregory Michaud (gregory.michaud@maine.edu)

from graphics import *
import random

width = 700
height = 700

def ColorSet(rect):
    r = random.random()
    if r < 0.09:
        # rect.setFill(color_rgb(0, 100, 25))
        rect.setFill(color_rgb(0, 50, 175))
    elif r < 0.15 and r >= 0.09:
        rect.setFill(color_rgb(65, 0, 100))
    elif r < 0.25 and r >= 0.15:
        rect.setFill(color_rgb(100, 0, 25))
    else:
        rect.setFill("white")

def deterSplit(win, w, h, x, y):
        ranNumW = random.uniform(90, w * 1.5)
        ranNumH = random.uniform(90, h * 1.5)
        
        # Recursive Case 1
        if w > width / 2 and h > height / 2:
            SplitBoth(win, w, h, x, y)
        elif w > width / 2:
            SplitVert(win, w, h, x, y)
        elif h > height / 2:
            SplitHori(win, w, h, x, y)
        
        # Recursive Case 2
        elif ranNumW < w or ranNumH < h:
        
            if (w < (width / 2) and w > 90) and (h < (height / 2) and h > 90):
                    SplitBoth(win, w, h, x, y)
            elif w < (width / 2) and w > 90:
                    SplitVert(win, w, h, x, y)
            elif h < (height / 2) and h > 90:
                    SplitHori(win, w, h, x, y)

        # Base Case
        else:
            rect = Rectangle(Point(x,y), Point(w+x, h+y))
            ColorSet(rect)   
            rect.setOutline("black")
            # rect.setWidth(3)
            rect.draw(win)

def SplitBoth(win, w, h, oriX, oriY):
    ranX = random.uniform((w*0.31),(w*0.68))
    ranY = random.uniform((h*0.31),(h*0.68))

    x1 = w - ranX
    # x2 = w - x1

    y1 = h - ranY
    # y2 = h - y1

    deterSplit(win, ranX, ranY, oriX, oriY)
    deterSplit(win, x1, ranY, oriX+ranX, oriY)
    deterSplit(win, ranX, y1, oriX, oriY+ranY)
    deterSplit(win, x1, y1, oriX+ranX, oriY+ranY)

def SplitVert(win, w, h, oriX, oriY):
    ranX = random.uniform((w*0.31),(w*0.68))
    # ranY = random.uniform((h*0.31),(h*0.68))

    x1 = w - ranX
    x2 = w - x1

    deterSplit(win, ranX, h, oriX, oriY)
    deterSplit(win, x1, h, oriX+ranX, oriY)

def SplitHori(win, w, h, oriX, oriY):
    # ranX = random.uniform((w*0.31),(w*0.68))
    ranY = random.uniform((h*0.31),(h*0.68))

    y1 = h - ranY
    y2 = h - y1

    deterSplit(win, w, ranY, oriX, oriY)
    deterSplit(win, w, y1, oriX, oriY+ranY)

def main():
    win = GraphWin("My Drawing", width, height)
    x = 0.0
    y = 0.0

    deterSplit(win, width, height, x, y)
    
    win.getMouse()
    win.close()
main()