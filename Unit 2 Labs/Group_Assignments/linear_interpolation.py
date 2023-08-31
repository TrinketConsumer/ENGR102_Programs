# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Katherine Johnson
# Sam Drake
# Pranav Koyande
# Section: 580
# Assignment: Lab 2.8
# Date: 31 August 2023

#Imports
from math import *
from math import pi

#Code
slope = (23027-2027)/(55-10)
t = 25
p = slope*(t - 10) + 2027
print("Part 1:")
print("For t = 25 minutes, the position p =", p, "kilometers")

radius = 6745
circum = 2*pi*radius
t = 300
p = slope*(t - 10) + 2027
p %= circum
print("Part 2:")
print("For t = 300 minutes, the position p =", p, "kilometers")