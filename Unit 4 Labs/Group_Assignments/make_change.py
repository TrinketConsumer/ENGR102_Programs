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
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = pay - cost
print(f"You received ${change:.2f} in change. That is... ")
pay *= 100
cost *= 100
change = pay - cost

quarters = 0
dimes = 0
nickels = 0
pennies = 0

if change >= 25:
    quarters = change // 25
    change -= quarters * 25

if change >= 10:
    dimes = change // 10
    change -= dimes * 10

if change >= 5:
    nickels = change // 5
    change -= nickels * 5

if change >= 1:
    pennies = change

if quarters > 0:
    if quarters > 1:
        print(f"{quarters:.0f} quarters")
    else:
        print(f"{quarters:.0f} quarter")

if dimes > 0:
    if dimes > 1:
        print(f"{dimes:.0f} dimes")
    else:
        print(f"{dimes:.0f} dime")

if nickels > 0:
    if nickels > 1:
        print(f"{nickels:.0f} nickels")
    else:
        print(f"{nickels:.0f} nickel")

if pennies > 0:
    if pennies > 1:
        print(f"{pennies:.0f} pennies")
    else:
        print(f"{pennies:.0f} penny")
