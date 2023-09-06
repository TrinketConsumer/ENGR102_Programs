# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 3.19
# Date: 6 September 2023

from math import *
from math import tau

#Recieves input and cuts at {x}
x = int(input("Please enter the number of digits of precision for tau: "))
print(f"The value of tau to {x} digits is: {tau:.{x}f}")