# with open("weather_data.csv", "r") as weather_file:
#     weather_data = weather_file.readlines()
#     # day = weather_data[0]."day"
#     print(weather_data)

# import csv
# with open("weather_data.csv", "r") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data)
# print(weather_data["temp"])

# weather_dict = weather_data.to_dict()
# print(f"weather dictionary: {weather_dict}")

# print(type(weather_data["temp"]))
# temp_list = weather_data["temp"].to_list()
# print(f"temperature list: {temp_list}")

# temp_average = weather_data["temp"].mean()
# print(f"average temperature: {temp_average}")

# temp_max = weather_data["temp"].max()
# print(f"max temperature: {temp_max}")

# print(weather_data['condition'])
# print(weather_data.condition)

# get data in row:
# print(weather_data.loc[1])
# print(weather_data[weather_data["day"] == "Monday"])

# find out the max tem of the day
# temp_max = weather_data["temp"].max()
# temp_max_day = weather_data[weather_data["temp"] == temp_max]
# print(temp_max_day["day"])

#find out Monday temp in F:
# monday = weather_data[weather_data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

#codes for central park squirrel file:
import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)
grey_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

grey_count = len(grey_squirrel["Hectare Squirrel Number"])
red_count = len(red_squirrel["Hectare Squirrel Number"])
black_count = len(black_squirrel["Hectare Squirrel Number"])

print(grey_count)
print(red_count)
print(black_count)

squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]

}

squirrel_dataFrame = pandas.DataFrame(squirrel_data_dict)
squirrel_dataFrame.to_csv("squirrel_data.csv")
print(squirrel_dataFrame)

