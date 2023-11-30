# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Section: 580
# Assignment: Lab 12.15
# Date: 14 November 2023
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
weather = open('WeatherDataCLL.csv', 'r')

head_line = weather.readline()
head_line = head_line.strip()
headers = head_line.split(',')

weather_dates = {}
counter = 0
max_temps = []
min_temps = []
for line in weather:
    line = line.strip()
    data = line.split(',')
    if data[0] == 'Date':
        continue
    today = data[0]
    weather_dates[today] = {}
    for i in range(1, len(data)):
        if data[i] == '':
            data[i] = None
        weather_dates[today][headers[i]] = data[i]
    if weather_dates[today][headers[5]] != None:
        max_temps.append(int(weather_dates[today][headers[5]]))
    if weather_dates[today][headers[6]] != None:
        min_temps.append(int(weather_dates[today][headers[6]]))

print(f'10-year maximum temperature: {max(max_temps)} F')  
print(f'10-year minimum temperature: {min(min_temps)} F')
print('')

month = input('Please enter a month: ')
year = input('Please enter a year: ')
print('')

month_dict = {'January' : '1', 'February' : '2', 'March' : '3', 'April' : '4', 'May' : '5', 'June' : '6', 'July' : '7', 'August' : '8', 'September' : '9', 'October' : '10', 'November' : '11', 'December' : '12'}
month_num = month_dict[month]

avg_temps = []
mean_humids = []
mean_winds = []
precip_yes = []
precip_tot = []
for date in weather_dates:
    date_list = date.split('/')
    if month_num == date_list[0] and year == date_list[2]:
        if weather_dates[date][headers[4]] != None:
            avg_temps.append(float(weather_dates[date][headers[4]]))
        if weather_dates[date][headers[3]] != None:
            mean_humids.append(float(weather_dates[date][headers[3]]))
        if weather_dates[date][headers[1]] != None:
            mean_winds.append(float(weather_dates[date][headers[1]]))
        if weather_dates[date][headers[2]] != None and weather_dates[date][headers[2]] != '0':
            precip_yes.append(float(weather_dates[date][headers[2]]))
        if weather_dates[date][headers[2]] != None:
            precip_tot.append(float(weather_dates[date][headers[2]]))
def average(variable):
    return sum(variable) / len(variable)

# print(f'For {month} {year}:')
# print(f'Mean average daily temperature: {round(average(avg_temps), 1)} F')
# print(f'Mean relative humidity: {round(average(mean_humids), 1)}%')
# print(f'Mean daily wind speed: {round(average(mean_winds), 2): .2f} mph')
# print(f'Percentage of days with precipitation: {round(((len(precip_yes) / len(precip_tot)) * 100), 1)}%')


weather.close()
