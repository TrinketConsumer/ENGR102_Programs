# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 4.16
# Date: 14 September 2023

from math import *

#Variable
num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))
num_3 = float(input("Enter number 3: "))

if num_1 >= num_2 and num_1 >= num_3:
    print(f"The largest number is {num_1:.1f}")
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"The largest number is {num_2:.1f}")
elif num_3 >= num_2 and num_3 >= num_1:
    print(f"The largest number is {num_3:.1f}")