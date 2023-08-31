# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 2.10
# Date: 31/8/2023

from math import *

#Variables
x1 = 8
x2 = -5
y1 = 6
y2 = 30
z1 = 7
z2 = 9
t1 = 12
t2 = 85
t3 = 30.0

xslope = (x2-x1)/(t2-t1)
yslope = (y2-y1)/(t2-t1)
zslope = (z2-z1)/(t2-t1)

x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print("At time", t3, "seconds:")
print("x1 = ", x_interpolation, "m")
print("y1 = ", y_interpolation, "m")
print("z1 = ", z_interpolation, "m")
print("-----------------------")

t3 = 37.5
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print("At time", t3, "seconds:")
print("x2 = ", x_interpolation, "m")
print("y2 = ", y_interpolation, "m")
print("z2 = ", z_interpolation, "m")
print("-----------------------")

t3 = 45.0
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print("At time", t3, "seconds:")
print("x3 = ", x_interpolation, "m")
print("y3 = ", y_interpolation, "m")
print("z3 = ", z_interpolation, "m")
print("-----------------------")

t3 = 52.5
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print("At time", t3, "seconds:")
print("x4 = ", x_interpolation, "m")
print("y4 = ", y_interpolation, "m")
print("z4 = ", z_interpolation, "m")
print("-----------------------")

t3 = 60.0
x_interpolation = xslope * (t3-t1) + x1
y_interpolation = yslope * (t3-t1) + y1
z_interpolation = zslope * (t3-t1) + z1
print("At time", t3, "seconds:")
print("x5 = ", x_interpolation, "m")
print("y5 = ", y_interpolation, "m")
print("z5 = ", z_interpolation, "m")