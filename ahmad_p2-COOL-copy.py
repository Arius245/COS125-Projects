# File: ahmad_p2-COOL-copy.py 
# Author: Arius Ahmad 
# Date: 11/18/22 
# Section: 1003 
# E-mail: arius.ahmad@maine.edu  
# Collaboration: I worked with McKade Wing (mckade.wing@maine.edu) and Gregory Michaud (gregory.michaud@maine.edu)

from graphics import *
import random

width = 700
height = 700

def ColorSetRGB(rect):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rect.setFill(color_rgb(r, g, b))

    # rect.setFill(color_rgb(r, 0, b))
    # rect.setFill(color_rgb(0, g, b))
    # rect.setFill(color_rgb(r, g, 0))

    # rect.setFill(color_rgb(0, 0, b))
    # rect.setFill(color_rgb(0, g, 0))
    # rect.setFill(color_rgb(r, 0, 0))

def ColorSetRB(rect):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rect.setFill(color_rgb(r, 0, b))

def ColorSetGB(rect):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rect.setFill(color_rgb(0, g, b))

def ColorSetRG(rect):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rect.setFill(color_rgb(r, g, 0))

def deterSplit(win, w, h, x, y):
        # ranNumW = random.uniform(5, w * .25)
        # ranNumH = random.uniform(5, h * .25)

        ranNumW = random.uniform(5, w * 1.5)
        ranNumH = random.uniform(5, h * 1.5)
        
        # Recursive Case 1
        # replaced all "/ 2" with "*0.05"
        if w > width *0.05 and h > height *0.05:
            SplitBoth(win, w, h, x, y)
        elif w > width *0.05:
            SplitVert(win, w, h, x, y)
        elif h > height *0.05:
            SplitHori(win, w, h, x, y)
        
        # Recursive Case 2
        # replaced all "/ 2" with "*0.05"
        elif ranNumW < w or ranNumH < h:
        
            if (w < (width *0.05) and w > 5) and (h < (height *0.05) and h > 5):
                    SplitBoth(win, w, h, x, y)
            elif w < (width *0.05) and w > 5:
                    SplitVert(win, w, h, x, y)
            elif h < (height *0.05) and h > 5:
                    SplitHori(win, w, h, x, y)

        # Base Case
        else:
            rect = Rectangle(Point(x,y), Point(w+x, h+y))
            
            # ColorSetRGB(rect)
            ColorSetRB(rect)
            # ColorSetGB(rect)
            # ColorSetRG(rect)
            # rect.setFill("white")
            
            rect.setOutline("black")
            # rect.setOutline("white")
            rect.setWidth(1)
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

    win.setBackground("black")
    deterSplit(win, width, height, x, y)
    
    # aCircle = Circle(Point(width/2,height/2), 175)
    # ColorSetRGB(aCircle)
    # aCircle.setWidth(5)
    # aCircle.draw(win)

    # bCircle = Circle(Point(width/2,height/2), 150)
    # ColorSetRGB(bCircle)
    # bCircle.setWidth(5)
    # bCircle.draw(win)

    # cCircle = Circle(Point(width/2,height/2), 125)
    # ColorSetRGB(cCircle)
    # cCircle.setWidth(5)
    # cCircle.draw(win)

    # dCircle = Circle(Point(width/2,height/2), 100)
    # ColorSetRGB(dCircle)
    # dCircle.setWidth(5)
    # dCircle.draw(win)

    # bingImage = Image(Point(width/2,height/2), "bing.gif")
    # bingImage.draw(win)

    # vincImage = Image(Point(width/2,height/2), "the.gif")
    # vincImage.draw(win)

    # message = Text(Point(350,350), "Bing Chilling")
    # message.setSize(20)
    # message.setStyle("bold")
    # message.setTextColor("white")
    # message.setFace("arial")
    # message.draw(win)

    win.getMouse()
    win.close()
main()