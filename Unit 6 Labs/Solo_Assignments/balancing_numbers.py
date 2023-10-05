# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.16
# Date: 2 October 2023

from math import *

x = int(input("Enter a value for n: "))
left_side = 0
right_side = 0
counter = x + 1
r = 0

for i in range(x):
    left_side += i
#Check for balancing number
while True:
    right_side += counter
    counter += 1
    r += 1
    if right_side == left_side:
        print(f"{x} is a balancing number with r={r}")
        break
    elif counter >= 10000000:
        print(f'{x} is not a balancing number')
        break
    else:
        continue