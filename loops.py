import turtle
from turtle import *
t = Turtle()
t.speed(0)



                
""" for i in range(60):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(5) """




""" def square(length, angle):
    for i in range(4):
        for j in range(4):
            t.forward(length)
            t.right(angle)
    t.right(5)

def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
addSquares(60) """



def star(length, angle):
    for i in range(5):
        for j in range(5):
            t.forward(length)
            t.right(144)
    t.right(5)

def starspiral(iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length += 5
starspiral(60)

turtle.done()