# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))


# sum_temp = 0
# for temp in temp_list:
#     sum_temp += temp
# ave_temp = sum_temp / len(temp_list)
# print(ave_temp)

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())

#Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Friday"])
#
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)

# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

## Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Hyeeun"],
#     "scores": [76, 66, 90]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
# colors_data = data["Primary Fur Color"].value_counts()
# colors_data.to_csv("squirrel_count.csv")
