# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 9 November 2023

#buh
x = input("Enter the name of the file: ")
file = open(x, 'r')
complete = open('valid_barcodes.txt', 'w')
b_list = []
valid = 0
for line in file:
    y = line.split('\n')
    b_list.append(y[0])
for element in b_list:
    counter = 0
    first_group = 0
    second_group = 0
    for i in element:
        counter += 1
        if counter == 13:
            second_group *= 3
            final_num = first_group + second_group
            final_num = str(final_num)
            final_digit = final_num[-1]
            if 10 - int(final_digit) == int(i):
                valid += 1
                complete.write(element + '\n')
        elif counter % 2 == 1:
            first_group += int(i)
        else:
            second_group += int(i)
print(f"There are {valid} valid barcodes")
file.close()
complete.close()
        