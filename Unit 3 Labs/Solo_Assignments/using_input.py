# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 3.17
# Date: 6 September 2023

from math import *
from math import pi

#Variable
print("This program calculates the applied force given mass and acceleration")
m = float(input("Please enter the mass (kg): "))
a = float(input("Please enter the acceleration (m/s^2): "))
f = m * a
print(f"Force is {f:.1f} N")

print("This program calculates the wavelength given distance and angle")
crystal_distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
w = 2*crystal_distance*sin((angle*pi)/180)
print(f"Wavelength is {w:.4f} nm")

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initial = float(input("Please enter the initial amount (g): "))
r = initial * (2 ** (-time/3.8))
print(f"Radon-222 left is {r:.2f} g")

print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
p = ((moles*8.314*temp)/volume)/1000
print(f"Pressure is {p:.0f} kPa")