# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.14
# Date: 2 October 2023

from math import *
#Define a function that checks if num is 0 or less, if yes then simply return 1. If not, return the original number * the same function subtracted by 2. This will loop until num is too small, then it'll stop.
def twofactorials(num):
    if num <= 0:
        return 1
    else:
        return num * twofactorials(num-2)