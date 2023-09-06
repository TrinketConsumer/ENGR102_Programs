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

#Function Def
def p_to_n(pounds):
    return pounds * 4.4482216153

def m_to_f(meters):
    return meters *  3.280839895

def atm_to_kpa(atm):
    return atm * 101.325

def watt_to_btu(watt):
    return watt * 3.412141633

def LperS_to_GperM(liters_per_second):
    return liters_per_second * 15.850323141489

def C_to_F(Celsius):
    return (Celsius * 9/5) + 32

x = float(input("Please enter the quantity to be converted: "))
print(f"{x:.2f} pounds force is equivalent to {p_to_n(x):.2f} Newtons")
print(f"{x:.2f} meters is equivalent to {m_to_f(x):.2f} feet")
print(f"{x:.2f} atmospheres is equivalent to {atm_to_kpa(x):.2f} kilopascals")
print(f"{x:.2f} watts is equivalent to {watt_to_btu(x):.2f} BTU per hour")
print(f"{x:.2f} liters per second is equivalent to {LperS_to_GperM(x):.2f} US gallons per minute")
print(f"{x:.2f} degrees Celsius is equivalent to {C_to_F(x):.2f} degrees Fahrenheit")