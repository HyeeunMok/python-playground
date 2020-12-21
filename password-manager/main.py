from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entries():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nWebsite: {website} "
                                                              f"\nEmail: {email} \nPassword: {password} "
                                                              f"\nIs it ok to save?")
        if is_ok:
            save_as_file(new_data)


def save_as_file(data):
    try:
        with open("data.json", mode="r") as data_file:
            #Reading old data
            json_data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    else:
        #Upadating old data with new data
        json_data.update(data)
        with open("data.json", mode="w") as data_file:
            #Saving updated data
            json.dump(json_data, data_file, indent=4)
            # data_file.write(f"\n{data}")
    finally:
        clear_entries()


def clear_entries():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "test@gmail.com")
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    search_keyword = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            loaded_json = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="No file", message="No Data File Found")
    else:
        if search_keyword in loaded_json:
            email = loaded_json[search_keyword]["email"]
            password = loaded_json[search_keyword]["password"]
            messagebox.showinfo(title="info", message=f"Website: {search_keyword} \nEmail: {email} "
                                                      f"\nPassword: {password}")
        else:
            messagebox.showwarning(title="No data", message=f"No details for the {search_keyword} exists.")
    finally:
        clear_entries()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manage")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "test@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


#Buttons

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=get_entries)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
