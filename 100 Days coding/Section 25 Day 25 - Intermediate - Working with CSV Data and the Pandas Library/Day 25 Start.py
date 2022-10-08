# with open ('weather_data.csv') as file:
#     data = file.readlines()  
#     print(data)

# import csv

# with open ('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

# This is a data frame
data = pandas.read_csv('weather_data.csv')
print(data)
print()
# data['temp'] is a series
print(data['temp'])
print()
# converting data frame to a dictionary
data_dict = data.to_dict()
print(data_dict)
print()
# converting series to a list
data_list = data['temp'].to_list()
print(data_list)

# get average of the temps
print(f'{sum(data_list)/len(data_list):.2f}')
print(f'{data["temp"].mean():.2f}')
print(data["temp"].max())

# get data from column
print(data['day'])
print(data.day)

# get data from row
print(data[data.day == 'Tuesday'])

# get the row of data which has the maximum temperature of the week
print(data[data.temp == data.temp.max()])

hot_day = data[data.temp == data.temp.max()]
print((hot_day.temp * 9/5) + 32)

# create data frame from scratch
new_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 32, 54]
}
data = pandas.DataFrame(new_dict)
print(data)
data.to_csv('new_data.csv')