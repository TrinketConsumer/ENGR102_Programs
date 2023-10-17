# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 6.16
# Date: 2 October 2023

vowels = ['a', 'e', 'i', 'o', 'u']
pig = input("Enter word(s) to convert to Pig Latin: ")
x = pig.split()
for i in x:
    for j in i:
        characters = []
        characters.append(j)
        if i.find(vowels) >= 0:
            print("trinkets")
        else:
            print("no trinkets")
