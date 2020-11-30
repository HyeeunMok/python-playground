from turtle import Turtle, Screen
import turtle as t
import random


tim = Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


# #### Random walk #####

# tim = Turtle()
# tim.shape("turtle")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(6)
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)


# #### draw several shapes #####

# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         tim.pensize(10)
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()