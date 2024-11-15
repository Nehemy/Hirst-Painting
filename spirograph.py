import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
turtle.colormode(255)
tom.shape("arrow")
tom.color("red")
tom.pensize(1)
tom.speed("fastest")

def colors():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    random_color = (r,g,b)
    return random_color


def draw_spirograph(size):
    for i in range(int(360 / size)):
        tom.color(colors())
        tom.setheading(tom.heading() + size)
        tom.circle(100)

draw_spirograph(1)

screen = Screen()
screen.exitonclick()
