import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
for i in range(10):
  a = random.randrange(1,100)
  leonardo.forward(a)
  b = random.randrange(1,100)
  michelangelo.forward(b)



michelangelo.up()
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
michelangelo.down()
leonardo.down()

# Part B - complete part B here
for sides in (3,4,6,9,12):
  for i in range(sides):
    michelangelo.forward(50)
    michelangelo.left(360/sides)
    leonardo.forward(50)
    leonardo.right(360/sides)
  leonardo.clear()
  michelangelo.clear()

window.exitonclick()
