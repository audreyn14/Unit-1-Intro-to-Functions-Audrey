""" import turtle as t

for i in range(60):
    print(i)

for i in range(60):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(5)

t.done() """

import turtle as t

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def triangle(x,y):
    for i in range(3):
        t.forward(x)
        t.left(y)
triangle(100,120)
