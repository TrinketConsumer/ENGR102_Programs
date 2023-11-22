# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

#As a team, we have gone through all required sections of the
#tutorial, and each team member undestands the material

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2.0,2.0)
y1 = (1/8) * (x**2)
y2 = (1/24) * (x**2)
plt.plot(x,y1,'r')
plt.plot(-x,y1,'r')
plt.plot(x,y2,'r')
plt.plot(-x,y2,'r')
plt.xlim(-2.0,2)
plt.show()