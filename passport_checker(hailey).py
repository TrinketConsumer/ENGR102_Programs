# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Hailey Wood
# Brendan Vohs
# Pranav Kakliya
# Ryan Mathews

# Section: 580
# Assignment: 4.15
# Date: 11/15/2023

file = input('Enter the name of the file: ')
outfile = open('valid_passports.txt', 'w')


with open(file, 'r') as passport:
    passport = passport.read()
    line = passport.split('\n\n')
    qual = []
    valid = 0
    for next_line in line:
        if 'byr' in next_line:
            qual += ['byr']
        if 'iyr' in next_line:
            qual += ['iyr']
        if 'eyr' in next_line:
            qual += ['eyr']
        if 'hgt' in next_line:
            qual += ['hgt']
        if 'hcl' in next_line:
            qual += ['hcl']
        if 'pid' in next_line:
            qual += ['pid']
        if 'cid' in next_line:
            qual += ['cid']
        if len(qual) == 7:
            valid += 1
            
            outfile.write(next_line)
            outfile.write('\n\n')
        qual = []
    print(f'There are {valid} valid passports')
    
outfile.close()
        
        
        #else:
            
    
        
    
    
    

