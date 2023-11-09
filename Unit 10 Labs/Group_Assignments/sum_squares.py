# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

from time import time
from math import sqrt

def list_nums(n):
    '''Improved solution'''
    for a in range(0, sqrt(n) + 1):
        for b in range(0, sqrt(n) + 1):
            for c in range(0, sqrt(n) + 1):
                d_squared = n - a**2 - b**2 - c**2
                d = int(d_squared**0.5)
                if d_squared == d**2 and a**2 + b**2 + c**2 + d**2 == n:
                    return [a, b, c, d]
    return None
# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(512)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result