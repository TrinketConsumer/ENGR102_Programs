# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 7.28
# Date: 16 October 2023

from math import *
x = int(input("Enter a four-digit integer: "))
counter = 0
recall = x
#Incredibly unoptomized, damien be sweet :(
while x != 6174:
    checker = 0
    if x == 0:
        print(0)
        print(f"{recall} reaches 0 via Kaprekar's routine in 1 iterations")
        break
    if x < 10:
        first_inverse = x
        second_inverse = 0
        third_inverse = 0
        fourth_inverse = 0
        first = 0
        second = 0
        third = 0
        fourth = x
        checker = 1
    elif x < 100:
        first_inverse = x // 10
        second_inverse = x - (first_inverse * 10)
        third_inverse = 0
        fourth_inverse = 0
        first = 0
        second = 0
        third = x // 10
        fourth = x - (third * 10)
        checker = 1
    elif x < 1000:
        first_inverse = x // 100
        second_inverse = (x - (first_inverse * 100)) // 10
        third_inverse = (x - (first_inverse * 100)) - (second_inverse * 10)
        fourth_inverse = 0
        first = 0
        second = x // 100
        third = (x - (second * 100) // 10)
        fourth = (x - (second * 100)) - (third * 10)
        checker = 1
    print(x, end = ' > ')
    counter += 1
    if checker != 1:
        first = x // 1000
        second = str(x)[1]
        third = str(x)[2]
        fourth = str(x)[3]
    x_list = [first, int(second), int(third), int(fourth)]
    x_list.sort()
    first_forward = x_list[0]
    second_forward = x_list[1]
    third_forward = x_list[2]
    fourth_forward = x_list[3]
    forward = str(first_forward) + str(second_forward) + str(third_forward) + str(fourth_forward)
    x_list.sort(reverse=True)
    if checker != 1:
        first_inverse = x_list[0]
        second_inverse = x_list[1]
        third_inverse = x_list[2]
        fourth_inverse = x_list[3]
    inverse = str(first_inverse) + str(second_inverse) + str(third_inverse) + str(fourth_inverse)
    x = int(inverse) - int(forward)
if x != 0:
    print('6174')
    print(f"{recall} reaches 6174 via Kaprekar's routine in {counter} iterations")