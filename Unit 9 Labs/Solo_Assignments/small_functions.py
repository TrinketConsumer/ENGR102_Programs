# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 25 October 2023
from math import pi, sqrt
def parta(r_sphere, r_hole):
    D_sphere = 2 * r_sphere #2r is equal to the diameter 
    VSphere = (4/3) * pi * r_sphere ** 3
    h = r_sphere - sqrt(r_sphere ** 2 - r_hole ** 2)
    VCap = (1/6) * pi * h * (3 * r_hole ** 2 + h ** 2)
    VCyl = pi * r_hole ** 2 * (D_sphere - 2*h) #the height of the cylinder is the diameter of the sphere minus the height of both caps
    VSphere_end = VSphere - 2 * VCap - VCyl
    return(VSphere_end)
#Recieve input for the target number
#Determine
def partb(n):
    odd_nums = []
    for i in range(1, (n // 2) + 1, 2): #from 1 to about half of n going by 2 (ensure oddness)
        odd_nums = []
        odd_sum = 0
        while odd_sum < n:
            odd_sum += i
            odd_nums.append(i)
            if odd_sum == n:
                return(odd_nums)
            i += 2
    return(False)

def partc(char, name, comp, email):
    if len(name) > len(comp) and len(name) > len(email):
        length = len(name) + 4
    elif len(comp) > len(name) and len(comp) > len(email):
        length = len(comp) + 4
    elif len(email) > len(name) and len(email) > len(comp):
        length = len(email) + 4
    card = ((char * (length + 2)) + '\n' + (char + name.center(length) + char) + '\n' + (char + comp.center(length) + char) + '\n' + (char + email.center(length) + char) + '\n' + (char * (length + 2)))
    return(card)
#DONE^
def partd(list):
    minimum = min(list)
    maximum = max(list)
    output = []
    list.sort()
    n = len(list)
    if n % 2 == 0:
        median = (list[n//2 - 1] + list[n//2]) / 2
    else:
        median = list[n//2]
    output = (minimum, int(median), maximum)
    return output
#DONE^
def parte(list1, list2):
    vel_list = []
    for i in range(len(list1) - 1):
        velocity = (list2[i+1] - list2[i]) / (list1[i+1] - list1[i])
        vel_list.append(velocity)
    return vel_list
#DONE^
def partf(list):
    for i in list:
        for j in list:
            if j + i == 2027:
                return j * i
    return False
#DONE^