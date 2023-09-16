# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Pranav Kakliya
# Brendan Vohs
# Hailey Wood
# Section: 580
# Assignment: Lab 4.13
# Date: 12 September 2023

from math import *

#Variables
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
print("The quadratic equation is", end = (' '))

if A != 0:
    if A == 1:
        print("x^2", end = (' '))
    elif A == -1:
        print("- x^2", end = (' '))
    elif A > 1:
        print(f"{A}x^2", end = (' '))
    elif A < 1 :
        print(f"- {abs(A)}x^2", end = (' '))

if B != 0:
    if B > 1:
        if A == 0:
            print(f'{B}x',end = (' '))
        elif A != 0:
            print(f'+ {B}x',end = (' '))
    elif B == -1:
        print('- x',end = (' '))
    elif B < 1:
        print(f'- {abs(B)}x',end = (' '))
    elif B == 1:
        if not A == 0:
            print('+ x',end = (' '))
        elif A == 0:
            print('x',end = (' '))
    elif B == -1:
        print('- x',end = (' '))

if C != 0:
    if C >= 1:
        print(f'+ {C}',end = (' '))
    elif C <= 1:
        print(f'- {abs(C)}', end = (' '))

print('= 0')