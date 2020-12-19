import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
STYLE = ('Courier', 12, 'normal')

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in guessed_states:
            state_list.remove(state)
        pandas.DataFrame(state_list).to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.pendown()
        t.write(f"{answer_state}", font=STYLE, align="center")



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
