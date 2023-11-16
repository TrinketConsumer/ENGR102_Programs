# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 14 November 2023

file = open("WeatherDataCLL.csv", "r")
lines = file.readlines()
line_counter = 0
max_temp = 0
min_temp = 20
header = []
for line in lines:
    if line_counter == 0:
        line_counter += 1
        line = line.strip()
        line = line.split(',')
        header.append(line)
        continue
    line = line.strip()
    line = line.split(',')
    print(line)
    if line[-2] != '' and int(line[-2]) > max_temp:
        max_temp = int(line[-2])
    if line[-1] != '' and int(line[-1]) < min_temp:
        min_temp = int(line[-1])
print(max_temp)
print(min_temp)
print(header)
