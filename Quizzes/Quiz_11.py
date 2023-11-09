a = 500

b = 500

c = 500

#Open the accounts text file, read each line, determine if subtraction or addition needs to #occur (and to which account), how much needs to be subtracted or removed, and then #update a, b, and c.

accounting = open('accounts.txt', 'r')

#Loop for every line

for line in accounting:

    #Split the line into a list on each space

    amount = line.split()

    #Run only once

    for i in range(0,1):

        #Determine if the first index of the list is a, b, or c. Determine if the second index                        #represents subtraction or addition. Perform the right function on the right account using         #the last index as an integer

        if amount[i] == 'a':

            if amount[i+1] == '>':

                a -= int(amount[i+2])

            else:

                a += int(amount[i+2])

        elif amount[i] == 'b':

            if amount[i+1] == '>':

                b -= int(amount[i+2])

            else:

                b += int(amount[i+2])

        else:

            if amount[i+1] == '>':

                c -= int(amount[i+2])

            else:

                c += int(amount[i+2])

print(f"The value of account a is {a}")

print(f"The value of account b is {b}")

print(f"The value of account c is {c}")

#Remember to close the file

accounting.close()