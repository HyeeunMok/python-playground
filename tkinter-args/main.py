from tkinter import *


def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)
    print("I got clicked!")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label["text"] = "New Text2"
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


window.mainloop()