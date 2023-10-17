# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ryan Mathews
# Pranav Kakliya
# Brendan Vohs
# Hailey Wood
# Section: 580
# Assignment: Lab 6.11
# Date: 3 October 2023

board = []
for i in range(9):
    temp_list = []
    for j in range(9):
        temp_list.append(0)
    board.append(temp_list)
x = 0
player = 1
while x != 'stop':
    if player == 1:
        print("BLACK'S TURN")
    elif player == 2:
        print("WHITE'S TURN")
    x = input("Enter the coordinate to place your stone (y) (enter stop to stop): ")
    if x == 'stop':
        break
    x = int(x)
    if x > 9:
        print("Invalid y coordinate, try again")
        continue
    y = input("Enter the coordinate to place your stone (x): ")
    y = int(y)
    if y > 9:
        print("Invalid x coordinate, try again")
        continue
    x -= 1
    y -= 1
    if x < 0:
        print("Invalid coordinate, try again")
        continue
    if y < 0:
        print("Invalid coordinate, try again")
        continue
    if board[x][y] == 0:
        player -= 1
        if player == 0:
            board[x][y] = 2
            player += 2
        elif player == 1:
            board[x][y] = 1
    else:
        print("Stone already there, try a different point")
        continue
    for i in board:
        for j in i:
            if j == 0:
                print('.', end = '')
            elif j == 1:
                print('o', end = '')
            elif j == 2:
                print('O', end = '')
        print()