# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 9 November 2023

#buh
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

v = np.array((0,1))
v.resize(2,1)
m = np.array((1.02, 0.095, -0.095, 1.02))
m.resize(2,2)
point = v
for i in range(0,250):
    point = m @ point
    plt.plot(point)
plt.xlabel("Various x-values from zero to one")
plt.ylabel("Various y-values from negative four-hundred to two-hundred")
plt.xlim(0,1)
plt.ylim(-450,250)
plt.title("Rainbow Lines In a Spiral")
plt.show()