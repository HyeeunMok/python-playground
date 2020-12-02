# import colorgram
#
# colors = colorgram.extract('color.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

color_list = [(232, 238, 246), (239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]


def new_start_position():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


def draw_painting(num_of_lines):
    i = 1
    while i <= num_of_lines:
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        new_start_position()
        i += 1


draw_painting(10)

screen = t.Screen()
screen.exitonclick()