# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Pranav Kakliya
# Brendan Vohs
# Hailey Wood
# Section: 580
# Assignment: Lab 6.11
# Date: 31 September 2023

from math import *

#Recieve input for side and layers
#first prism is side * side * 3 to get the rectangles all around the prism
#Top of the first prism is (sqrt(3)/4) * (side**2) to get the equilateral triangle on top
#The next layer has the same height but the side length is equal to layers * side to make one big rectangle on each side.
#Change equation to side * (side * layers) * 3 to account for this.
#Top of this layer has a new side length now which is equal to layers * side.
#Change equation to (sqrt(3)/4) * ((layers*side)**2) to account for this.
#The previous layer blocks a portion of the area just calculated.
#To account for this subtract the previous layer's top area from the total area.
#Surface area equation is (side * (side * layers) * 3) + (sqrt(3)/4) * ((layers*side)**2)
#Total area equation is surface area - ((sqrt(3)/4) * (((layers-1)*side)**2))
#To account for the changing layers subtract one from layers every time code loops
#Code should only run while layers is greater than 0
#To account for this add while layers > 0

side = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
surface_area = 0
total_surface_area = 0

while layers > 0:
    surface_area = (side * (side * layers) * 3) + ((sqrt(3)/4) * ((layers * side)**2))
    surface_area -= ((sqrt(3)/4) * (((layers-1)*side)**2))
    layers -= 1
    total_surface_area += surface_area

print(f'You need {total_surface_area:.2f} m^2 of gold foil to cover the pyramid')
