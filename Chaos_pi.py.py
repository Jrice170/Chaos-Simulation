

"""This code it going to randamly generate dots on to a graphics window.
The code below will do a calulation for random dots.
This code will allso show the calculation for the percentage that hit the circle.

first import the random modual 'from random import *'
next import the graphics modual. 'from graphics import *
import math 
1. input the number of dots generated
2. outputs generate the graphic picture of what is happening
"""
from random import *
import math
from graphics import *


## function for the whole background the the graphical picture


win = GraphWin("Pi Simulation",600,600)
win.setBackground("purple")
center = Point(0,0)

##Corrds

win.setCoords(10,-10,-10,10)

##for the rectange
   
rect = Rectangle(Point(-4,-4),Point(4,4))
rect.setOutline("black")
rect.setFill("red")
rect.setWidth(1)
rect.draw(win)

Display_text = Text(Point(2,-6),"Enter Total Number of dots. ")
Display_text.draw(win)

dis = Entry(Point(-2,-6),3)
dis.getText

dis.draw(win)


    ## this draws the simulated circle


cir = Circle(center,4)
cir.setOutline("red")
cir.setWidth(3)
cir.setFill("black")
cir.draw(win)

enter_box = Rectangle(Point(-1,1),Point(1,-1))
enter_box.move(-5,-5)
enter_box.move(0,-1)
Word_enter = Text(Point(-5,-6),"Enter")
Word_enter.draw(win)
enter_box.draw(win)
## tells user how to end program
Kill_while = Text(Point(1,-8),"To kill while Loop <ENTER> interger 0")
Kill_while.draw(win)

    ### draws each individual point 
 ### this function draws all of the objects 


##        number_dots = eval(input("enter the number of dots: "))
##        n = 1 ## range stops before the number you put in>>>
##        Total_darts = n + number_dots
##        hits = 0
### TAKE NOTE** I ADDED A WHILE LOOP TO MAKE MY PROGRAM MORE USER Friendly
##      What THE WHILE LOOP DOES:: WILL Continue RUNING AS LONG AS THE USER DOES NOT ENTER A LETTER
##win.getMouse()

## while state does not have a string in it will continue running
## loop will run while* the input does not equal zero.
while True:

    win.getMouse()
    try:
        number_dots = eval(dis.getText())
    except SyntaxError:
        Text(Point(4,-7),"The end").draw(win)
        break 
    
##      
    ## range stops before the number you put in>>>
    Total_darts = 1 + number_dots
    hits = 0
    #state = input("Hit Enter to quit")
    
## I Without THE IF STATEMENT THE LOOP Would BE INFINITE. 
    if number_dots == 0:
        break
   
    
#### This for loop WILL LOOP HOW MANY TIMES THE USER INPUTS FOR TOTAL_DARTS
    for i in range(0,Total_darts):
        ####
        x = random()*8 - 4
        ####
        y = random()*8 - 4
        ##
        p = Point(x,y)
        blue = "blue"
        p.draw(win)
        p.setFill(blue)

        ##
        in_circle = x**2 + y**2
                
        if in_circle <= 16:
            hits += 1
                   
  ##          calculations
    pi = 4 *(hits/Total_darts)
    ave = hits/Total_darts
    
    dis_play = Text(Point(5,6)," ")
    dis_play_2 = Text(Point(5,5)," ")
    play = Entry(Point(0,6),7)
    play_2 = Entry(Point(0,5),7)
    play.draw(win)
    play_2.draw(win)
    
    dis_play.setText("Percent That hit the circle:")
    dis_play_2.setText("The average of pi" + "~")
    play.setText(str(round(ave*100,2)) + "%")
    play_2.setText(str(round(pi,3)))
    dis_play.draw(win)
    dis_play_2.draw(win)

try:
    win.close(win)
except TypeError:
    Text(Point(4,-9),"THE STORM HAS PASSED !!!!!!").draw(win)

        
            

