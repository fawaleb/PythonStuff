import turtle


def square(dist,ang):
    pete_turtle = turtle.Turtle()
    pete_turtle.forward(dist)
    pete_turtle.right(ang)
    pete_turtle.forward(dist)
    pete_turtle.right(ang)
    pete_turtle.forward(dist)
    pete_turtle.right(ang)
    pete_turtle.forward(dist)


# Instruct Turtle to make a square
square(100,90)
square(100,-90)
square(-100,90)
square(-100,-90)
