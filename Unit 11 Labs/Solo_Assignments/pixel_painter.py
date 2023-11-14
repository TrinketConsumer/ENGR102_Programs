# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 14 November 2023

#buh
x = input("Enter the filename: ")
char = input("Enter a character: ")
trinket = []
file = open(x, "r")
y = x[0:-3] + "txt"
complete = open(y, "w")
lines = file.readlines()
for line in lines:
    line = line.strip()
    line = line.split(',')
    counter = 0
    for i in line:
        counter += 1
        if counter % 2 == 1:
            for j in range(0, int(i)):
                complete.write(' ')
        else:
            for j in range(0, int(i)):
                complete.write(char)
    complete.write('\n')
complete.close()
file.close()
print(f"{x[0:-3]}txt created!")