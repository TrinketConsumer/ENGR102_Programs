# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ryan Mathews
# Section: 580
# Assignment: word_puzzle
# Date: 01 11 2023

def get_valid_letters(puzzlestring): 
    uniqueletters = ''
    for i in puzzlestring:
        if i not in uniqueletters and i.isalpha(): #make sure its not already there, and it is a word
            uniqueletters += i
    return uniqueletters

def is_valid_guess(str1, str2):
    list1 = list(str1)
    list1.sort() #check if guess is valid
    list2 = list(str2)
    list2.sort()
    if list1 == list2:
        return True
    return False

def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == ((quotient * divisor) + remainder): #check if guess is correct
        return True
    return False

def make_number(word, guess):
    #convert the guess into a list
    guess_list = list(guess)
    mynum = ''
    for i in word:
        if i in guess_list:
            mynum += str(guess_list.index(i))
    try:                                        #zybooks giving error for 1/20 trials and this try/except loop fixed it?
        return int(mynum)
    except:
        print('Your guess should contain exactly 10 unique letters used in the puzzle.')
        exit()

def make_numbers(puzzle,guess):
    puzzle = puzzle.split(',')
    divi = puzzle[1].split() #to be able to index the divided and divisor
    mytuple = (make_number(divi[-1],guess) , make_number(puzzle[0],guess) , make_number(divi[0],guess) , make_number(puzzle[-1],guess))
    return mytuple

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    guess = input('\nEnter your guess, for example ABCDEFGHIJ: ')
    if len(guess) != 10:
        print('Your guess should contain exactly 10 unique letters used in the puzzle.')
        return

    x = is_valid_guess(get_valid_letters(puzzle),guess)
    mytuple = make_numbers(puzzle,guess)  
    correct = check_user_guess(mytuple[0] , mytuple[1] , mytuple[2] , mytuple[3])

    if x == True and (correct == True):
        print('Good job!')
    else:
        print('Try again!')

if __name__ == '__main__':
    main()