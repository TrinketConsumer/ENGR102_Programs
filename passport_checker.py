
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Brendan Vohs
# Ryan Matthews 
# Pranav Kakilya
# Hailey Wood
# Section: 580
# Assignment: Team Lab Topic 3
# Date: 09/12/23
#
#
# YOUR CODE HERE

passport_input = input('Enter the name of the file: ')
passport_file = open(passport_input, 'r')
valid_passports = open('valid_passports.txt', 'w')

passport_string = passport_file.read()
passport_list = passport_string.split('\n\n')
counter = 0
for passport in passport_list:
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'pid' in passport and 'cid' in passport:
        counter += 1
        valid_passports.write(passport + '\n\n')
print(f'There are {counter} valid passports')
passport_file.close()
valid_passports.close()