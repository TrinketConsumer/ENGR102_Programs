# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Pranav Kakliya
# Brendan Vohs
# Hailey Wood
# Section: 580
# Assignment: Lab 3.15
# Date: 5 September 2023

from math import *

#Inputs
t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))
t3 = t1

xslope = (x2-x1)/(t2-t1)
yslope = (y2-y1)/(t2-t1)
zslope = (z2-z1)/(t2-t1)

x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print(f"At time {t3:.2f} seconds the object is at ({x_interpolation:.3f}, {y_interpolation:.3f}, {z_interpolation:.3f})")
'''t3 is redefined before calculating the new inteerpolation everytime. The new definition splits 
the final time subtracted from the beginning time in 4, multiplies the result by the number of times the code has already been run, and then adds the original time back in'''
t3 = ((t2 - t1) / 4) + t1
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print(f"At time {t3:.2f} seconds the object is at ({x_interpolation:.3f}, {y_interpolation:.3f}, {z_interpolation:.3f})")
t3 = (((t2 - t1) / 4) * 2) + t1
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print(f"At time {t3:.2f} seconds the object is at ({x_interpolation:.3f}, {y_interpolation:.3f}, {z_interpolation:.3f})")
t3 = (((t2 - t1) / 4) * 3) + t1
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print(f"At time {t3:.2f} seconds the object is at ({x_interpolation:.3f}, {y_interpolation:.3f}, {z_interpolation:.3f})")
t3 = t2 
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print(f"At time {t3:.2f} seconds the object is at ({x_interpolation:.3f}, {y_interpolation:.3f}, {z_interpolation:.3f})")