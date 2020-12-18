import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
word = Turtle()
word.hideturtle()
style = ('Courier', 12, 'normal')
game_over_style = ('Courier', 18, 'normal')
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
state_dict = data.to_dict()

correct_answers = []
correct_answers_count = 0

game_is_on = True
while game_is_on:
    if answer_state in state_list:
        state_x_cor = int(data[data.state == answer_state].x)
        state_y_cor = int(data[data.state == answer_state].y)
        word.penup()
        word.goto(state_x_cor, state_y_cor)
        word.pendown()
        word.write(f"{answer_state}", font=style, align="center")
        correct_answers.append(answer_state)
        correct_answers_count += 1
        answer_state = screen.textinput(title=f"{correct_answers_count}/50 States Correct", prompt="What's another state's name?").title()
        print(correct_answers)
    else:
        print("Not there")
        word.penup()
        word.goto(0, 0)
        word.pendown()
        word.write("Game Over!", font=game_over_style, align="center")
        game_is_on = False

screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
