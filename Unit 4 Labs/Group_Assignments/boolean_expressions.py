# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Pranav Kakliya
# Brendan Vohs
# Hailey Wood
# Section: 580
# Assignment: Lab 4.14
# Date: 14 September 2023

from math import *

############ Part A ############
A = input("Enter True or False for a: ")
B = input("Enter True or False for b: ")
C = input("Enter True or False for c: ")

if A == "t" or A == "T" or A == "True":
    A = True
elif A == "f" or A == "F" or A == "False":
    A = False
if B == "t" or B == "T" or B == "True":
    B = True
elif B == "f" or B == "F" or B == "False":
    B = False
if C == "t" or C == "T" or C == "True":
    C = True
elif C == "f" or C == "F" or C == "False":
    C = False

############ Part B ############
trinkets = (A and B and C)
not_trinkets = (A or B or C)
print(f"a and b and c: {trinkets}")
print(f"a or b or c: {not_trinkets}")

############ Part C ############
xor = (A and not B) or (not A and B)
odd_number = (not A and not B and C) or (not A and B and not C) or (A and not B and not C) or (A and B and C)
print(f"XOR: {xor}")
print(f"Odd number: {odd_number}")

