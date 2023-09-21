# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 4.18
# Date: 14 September 2023

from math import *
gadgets = 0
days = int(input("Please enter a positive value for day: "))
#Logic to determine which formula to use for days
if days < 0:
    print("You entered an invalid number!")
elif days <= 10:
    gadgets = int(days * 10)
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')
elif days < 50:
    gadgets = int((10*10) + ((days - 10) *((11+days)/2)))
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')
elif days > 101:
    print(f"The sum total number of gadgets produced on day {days} is 3820")
elif days >= 50:
    gadgets = int(1270 + (days - 49) * (50))
    print(f"The sum total number of gadgets produced on day {days} is {gadgets}")
