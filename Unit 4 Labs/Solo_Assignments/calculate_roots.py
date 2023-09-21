# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 4.19
# Date: 19 September 2023

from math import *
#Get input from user
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))
if a < 1 and b < 1:
    print("You entered an invalid combination of coefficients!")
elif a < 1:
    root = float(-c / b)
    print(f"The root is x = {root:.1f}")
else:
    root_positive = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    root_negative = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
if root_positive == root_negative:
    print(f"The root is x = {root_positive:.1f}")
else:
    print(f"The roots are x = {root_positive:.1f} and x = {root_negative:.1f}")