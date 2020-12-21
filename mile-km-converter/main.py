from tkinter import *


def convert_mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

FONT_STYLE = ("Arial", 15)
#Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Label
mile_label = Label(text="Miles", font=FONT_STYLE)
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT_STYLE)
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=FONT_STYLE)
km_result_label.grid(column=1, row=1)

km_label = Label(text="km", font=FONT_STYLE)
km_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=convert_mile_to_km)
button.grid(column=1, row=2)


window.mainloop()