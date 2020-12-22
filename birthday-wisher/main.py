##################### Normal Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "*******.cs@gmail.com"
PASSWORD = "*******"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (name, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    print(file_path)
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")



