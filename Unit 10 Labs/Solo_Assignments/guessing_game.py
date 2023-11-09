# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: RYAN MATHEWS
# Section: 580
# Assignment: Lab 9.16
# Date: 25 October 2023
def starter():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
#Trinkets
def logic():
    counter = 0
    y = 0
    while True:
        if y != 0:
            pass
        else:
            x = input("What is your guess?")
        secret_num = 27
        try:
            int(x)
        except:
            x = input("Bad input! Try again: ")
            y = 1
            continue
        y = 0
        x = int(x)
        if x == secret_num:
            counter += 1
            print(f"You guessed it! It took you {counter} guesses.")
            break
        elif x > secret_num:
            counter += 1
            print("Too high!")
            continue
        elif x < secret_num:
            counter += 1
            print("Too low!")
            continue
starter()
logic()