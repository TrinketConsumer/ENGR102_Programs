# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 5.4
# Date: 27 September 2023
from math import *

#Calculating slope using the formula given
excess_temp = float(input("Enter the excess temperature: "))
#Slope 1 is calculated using the first two points on the graph
slope_1 = log10(7000/1000) / log10(5/1.3)
#Slope 2 is calculated using the 2nd and 3rd points on the graph
slope_2 = log10((1.5e6)/7000) / log10(30/5)
#Slope 3 is calculated using the 3rd and 4th points on the graph
slope_3 = log10((2.5e4)/(1.5e6)) / log10(120/30)
#Slope 4 is calculated using the 4th and 5th points on the graph
slope_4 = log10((1.5e6)/(2.5e4)) / log10(1200/120)
#Interpolation is calculated using the formula
#y = initial_y * (excess_temp / initial_x) ^ slope_x
#slope_x is the slope that is relevant for the excess_temp given
interpolation_1 = 1000 * (excess_temp/1.3)**slope_1
interpolation_2 = 7000 * (excess_temp/5)**slope_2
interpolation_3 = (1.5e6) * (excess_temp/30)**slope_3
interpolation_4 = (2.5e4) * (excess_temp/120)**slope_4

#Logic to check where the excess_temp falls
#If excess temp is less than the first point on the graph interpolation cannot occur
#That would be called extrapolation
if excess_temp < 1.3:
    print("Surface heat flux is not available")
elif excess_temp <= 5:
    print(f'The surface heat flux is approximately {interpolation_1:.0f} W/m^2')
elif excess_temp <= 30:
    print(f'The surface heat flux is approximately {interpolation_2:.0f} W/m^2')
elif excess_temp <= 120:
    print(f'The surface heat flux is approximately {interpolation_3:.0f} W/m^2')
elif excess_temp <= 1200:
    print(f'The surface heat flux is approximately {interpolation_4:.0f} W/m^2')
else:
    print("Surface heat flux is not available")
#If the excess temp is greater than the last point on the graph the same rule applies
#This would also be called extrapolation