# import colorgram
#
# image_colors = []
# colors = colorgram.extract("image.jpg",100)
# for _ in colors:
#     color = colors[_]
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     image_colors.append(new_color)

import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
turtle.colormode(255)
tom.shape("arrow")
tom.speed("fastest")
tom.hideturtle()

rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

y_value = -250
while y_value <= 200:
    for _ in range(-250, 201, 50):
        if _ <= 200:
            tom.teleport(_, y_value)
            tom.dot(20, random.choice(rgb_colors))
    y_value += 50

screen = Screen()
screen.exitonclick()