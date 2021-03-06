# THIS SHOULD ALWAYS BE YOUR FIRST LINE
from Myro import *
init("sim") #if your simulator is not running

def squareside(): #function for first three sides of square
    forward(2,2)
    wait(.5)
    turnBy(90)
  
def triangleside(): #function for first two sides of triangle
    penDown()
    forward(1,2)
    penUp()
    wait(.1)
    turnBy(120)

#SQUARE BEGINS
penDown()
squareside()
squareside()
squareside()
forward(2,2)
penUp()

#MOVE TO START LOCATION OF TRIANGLE
forward(1,1)

#TRIANGLE BEGINS
triangleside()
triangleside()
penDown()
forward(1,2.1)
penUp()
wait(.5)

#MOVE TO STARTING LOCATON OF LETTER T
forward(1.5,2)
turnLeft(1,1)
forward(1.8,1)

#LETTER T BEGINS
penDown()
forward(2,1)
penUp()
backward(1,1)
turnBy(90)
penDown()
forward(2,1)
penUp()
wait(.5)

#MOVE TO STARTING LOCATION OF LETTER K
forward(.5,1)

#LETTER K BEGINS
penDown()
forward(2,1)
penUp()
backward(1,1)
turnBy(45)
penDown()
forward(.7,2)
penUp()
backward(.7,2)
wait(.5)
turnBy(90)
penDown()
forward(1.5,1)
penUp()

forward(3,1)