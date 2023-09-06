# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 3.18
# Date: 6 September 2023

from math import *

#Define Functions
def triangle(a):
    return (sqrt(3)/4) * (a ** 2)

def square(a):
    return a ** 2

def pentagon(a):
    return .25 * sqrt(5 * (5 + (2 * sqrt(5)))) * (a ** 2)

def dodecagon(a):
    return 3 * (2 + sqrt(3)) * (a ** 2)

a = float(input("Please enter the side length: "))
print(f"A triangle with side {a:.2f} has area {triangle(a):.3f}")
print(f"A square with side {a:.2f} has area {square(a):.3f}")
print(f"A pentagon with side {a:.2f} has area {pentagon(a):.3f}")
print(f"A dodecagon with side {a:.2f} has area {dodecagon(a):.3f}")