# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.15
# Date: 2 October 2023

from math import *
x = int(input("Enter a positive integer: "))
counter = 0
print(f'The Juggler sequence starting at {x} is: ')
#Check if the integer given is one, if yes then skip the while loop and simply output 1 with 0 iterations.
if x != 1:
    print(f'{x:.0f},', end = ' ')
    while True:
        if x == 2:
            print("1", end = ' ')
            counter += 1
            break
        elif x % 2 == 0:
            x = (sqrt(x)) // 1
            print(f'{x:.0f},', end = ' ')
            counter += 1
        elif x % 2 == 1:
            x = (x**(3/2)) // 1
            print(f'{x:.0f},', end = ' ')
            counter += 1
else:
    print("1", end = ' ')
print(f'\nIt took {counter} iterations to reach 1')