# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.16
# Date: 2 October 2023

#super trinket time
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
pig = input("Enter word(s) to convert to Pig Latin: ")
x = pig.split()
characters = []
counter = 0
new = ''
for i in x:
    for j in i:
        if j in vowels:
            new += str(i) + 'yay' + ' '
            break
        elif str(i)[1] in vowels:
            new += str(i)[1:] + str(j) + 'ay' + ' '
            break
        elif str(i)[2] in vowels:
            new += str(i)[2:] + str(j) + str(i)[1] + 'ay' + ' '
            break
print(f'In Pig Latin, "{pig}" is : {new}')
        

        