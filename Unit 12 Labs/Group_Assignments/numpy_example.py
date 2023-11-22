# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Mathews
# Section:      580
# Assignment:   Lab 12
# Date:         21 November 2023

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np
from numpy import sqrt
import matplotlib as mlp
import matplotlib.pyplot as plt

a = np.arange(0,12)
a.resize(3,4)
b = np.arange(0,8)
b.resize(4,2)
c = np.arange(0,6)
c.resize(2,3)
print(f"A = {a}")
print()
print(f"B = {b}")
print()
print(f"C = {c}")
print()
temp = np.dot(a,b)
d = np.dot(temp, c)
print(f"D = {d}")
print()
dt = np.transpose(d)
print(f"D^T = {dt}")
print()
e = sqrt(d) / 2
print(f"E = {e}")