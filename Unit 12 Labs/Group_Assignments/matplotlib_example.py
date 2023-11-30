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

t = np.arange(0.01, 20.0, 0.001) 
data1 = np.exp(t) 
data2 = np.sin(0.3 * np.pi * t) 
   
fig, ax1 = plt.subplots() 
   
color = 'tab:blue'
ax1.set_xlabel('time (s)') 
ax1.set_ylabel('exp', color = color) 
ax1.plot(t, data1, color = color) 
ax1.tick_params(axis ='y', labelcolor = color) 

ax2 = ax1.twinx() 
   
color = 'tab:green'
ax2.set_ylabel('sin', color = color) 
ax2.plot(t, data2, color = color) 
ax2.tick_params(axis ='y', labelcolor = color) 
plt.show() 