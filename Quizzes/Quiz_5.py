from math import *

#Recieve input for the integer and power

number = int(input("Enter a 4-digit integer: "))

power = int(input("Enter the power: "))

#Calculate out each part of the integer

first = number // 1000

second = (number % 1000) // 100

third = ((number % 1000) - (second * 100)) // 10

fourth = ((number % 1000) - (second * 100)) % 10

#Calculate each part to the power given

power_one = first ** power

power_two = second ** power

power_three = third ** power

power_four = fourth ** power

sum_power = power_one + power_two + power_three + power_four

#Determine if the sum of those parts is the same is the original input

if sum_power == number:

    print(f'{number} with given power {power} is a PDI')

else:

    print(f'{number} with given power {power} is NOT a PDI')