#******************************************************************************
# stack.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Overall notes (not to replace inline comments):
    

import turtle
import math

screen = turtle.Screen()
block = turtle.Turtle()


n = int(input("Enter an integer for n: "))

for row in range(n):

    for i in range(4):
        block.forward(10)
        block.left(90)
    

    block.right(90)
    block.penup()
    block.forward(10)
    block.left(90)
    block.forward(10)
    block.pendown()
