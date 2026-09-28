import turtle

# create a Turtle instance and make drawing fast
t = turtle.Turtle()
t.speed(0)

sidelength = 100
rotate = 90

def square(x, y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def triangle(x, y):
    for i in range(3):
        t.forward(x)
        t.left(y)

triangle(100, 120)

turtle.done()

