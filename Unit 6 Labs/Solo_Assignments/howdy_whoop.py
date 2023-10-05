# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.13
# Date: 2 October 2023

from math import *
#Checking if i is divisble by the inputs
x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
for i in range (1,101):
    if i % x == 0 and i % y == 0:
        print("Howdy")
        print("Whoop")
    elif i % x == 0:
        print("Howdy")
    elif i % y == 0:
        print("Whoop")
    else:
        print(i)