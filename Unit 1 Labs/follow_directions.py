# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 1.13
# Date: 22/8/2023

from math import *
from math import pi

#Details
print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My terrible guess is 3")

#Variables
x = 1.1

#Program
s = (sin(x-1)/(x-1))
print(s)
x = 1.01
s = (sin(x-1)/(x-1))
print(s)
x = 1.001
s = (sin(x-1)/(x-1))
print(s)
x = 1.0001
s = (sin(x-1)/(x-1))
print(s)
x = 1.00001
s = (sin(x-1)/(x-1))
print(s)
x = 1.000001
s = (sin(x-1)/(x-1))
print(s)
x = 1.0000001
s = (sin(x-1)/(x-1))
print(s)
x = 1.00000001
s = (sin(x-1)/(x-1))
print(s)
x = 1.000000001
print()
print("My guess was way off")
