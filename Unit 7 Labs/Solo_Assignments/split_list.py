# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.16
# Date: 2 October 2023

#Trinket time
x = input("Enter numbers: ")
x_list = x.split()
left_list = []
right_list = []
left_sum = 0
right_sum = 0
for i in x_list:
    right_sum += int(i)
    right_list.append(i)
while left_sum != right_sum:
    for i in x_list:
        left_sum += int(i)
        left_list.append(i)
        right_sum -= int(i)
        right_list.remove(i)
        if left_sum == right_sum:
            break
    if left_sum == right_sum:
        break
    else:
        print("Cannot split evenly")
left_int_list = []
right_int_list = []
for i in left_list:
    left_int_list.append(int(i))
for i in right_list:
    right_int_list.append(int(i))
print(f"Left: {left_int_list}")
print(f"Right: {right_int_list}")
print(f"Both sum to {left_sum}")