import smtplib

# Replace to your email and password
my_email = "******.cs@gmail.com"
password = "******"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="*****@naver.com",
        msg="Subject:Hello\n\nThis is the body of my email.")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year == 2020:
#     print("Wear a face mask!")
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=14)
# print(date_of_birth)