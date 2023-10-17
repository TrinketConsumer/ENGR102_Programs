# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.16
# Date: 2 October 2023

#Make dictionary
leet_dict = {'a' : 4, 'e' : 3, 'o' : 0, 's' : 5, 't' :7}
x = input("Enter some text: ")
y = x.split()
final_string = ''
for i in y:
    temp_string = ''
    for j in i:
        if j in leet_dict:
            temp_string += str(leet_dict.get(j))
        else:
            temp_string += j
    final_string += temp_string
    final_string += ' '
print(f'In leet speak, "{x}" is: ')
print(final_string)