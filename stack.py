#******************************************************************************
# stack.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Overall notes (not to replace inline comments):
    

import turtle

screen = turtle.Screen()
block = turtle.Turtle()
  
def draw():

  for i in range(4):
    block.forward(10)
    block.left(90)


n = int(input("Enter an integer for n: "))

for row in range(n):
    for i in range(row+1):
        draw()
        block.forward(10)
    
    block.penup()
    block.right(90)
    block.forward(10)
    block.right(90)
    block.forward((row+1)*10)
    block.right(180)
    block.pendown()
    

