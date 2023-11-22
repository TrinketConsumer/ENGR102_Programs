# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:40:26 2023

@author: hobbi
"""
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
from string import ascii_lowercase as abc
passport_input = input('Enter the name of the file: ')
passport_file = open(passport_input, 'r')
valid_passports2 = open('valid_passports2.txt', 'w')

passport_string = passport_file.read()
passport_list = passport_string.split('\n\n')
counter = 0
check = 0
for passport in passport_list:
    check = 0
    try:
        num = passport.index('byr')
        if int(passport[num + 4:num + 8]) <= 2007 and int(passport[num + 4:num + 8]) >= 1920: #checks if birthyear is valid
            check += 1
            
        num = passport.index('iyr')
        if int(passport[num + 4:num + 8]) <= 2023 and int(passport[num + 4:num + 8]) >= 2013: #checks if issue is valid
            check += 1
            
        num = passport.index('eyr')
        if int(passport[num + 4:num + 8]) <= 2033 and int(passport[num + 4:num + 8]) >= 2023: #checks if expiration is valid
            check += 1
            
        num = passport.index('hgt')
        if 'in' in passport[num + 6:num + 8]:
            height = int(passport[num + 4:num + 6]) #this is chcecking if heigh is valid in inches
            if height >= 59 and height <= 76:
                check += 1
        elif 'cm' in passport[num + 7:num + 9]:
            height = int(passport[num + 4:num + 7]) #check if height is valid in cm
            if height >= 150 and height <= 193:
                check += 1
        
        num = passport.index('hcl')
        for i in range(6, len(abc)):
            if abc[i] in passport[num + 5:num + 11]: #loops through the letters g-z to see if any of them are used in code
                raise ValueError
        if passport[num + 4] != '#': #checking if it starts with a '#'
            raise ValueError
        if ' ' not in passport[num + 5:num + 11] and '\n' not in passport[num + 5:num + 11]: 
            check += 1 #checks if it is 6 characters long by checking for any white space in the value
        
        
        num = passport.index('pid')
        for i in range(num + 4, num + 13):
            try:
                float(passport[i])
            except:
                raise ValueError
        check += 1
        
        
        num = passport.index('cid')
        if ' ' not in passport[num + 4:num + 7] and '\n' not in passport[num + 4:num + 7]:
            check += 1
        if passport[num + 4] == '0': #checks to make sure it does not lead with 0
            raise ValueError
        
        if check == 7:
            counter += 1
            valid_passports2.write(passport + '\n\n')
        
    except ValueError:
        continue
    
print(f'There are {counter} valid passports')
passport_file.close()
valid_passports2.close()