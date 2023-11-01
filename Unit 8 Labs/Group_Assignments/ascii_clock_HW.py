time = input('Enter the time: ')
time_list = list(time)
clock_type =  int(input('Choose the clock type (12 or 24): '))
mychar = input('Enter your preferred character: ')
space = ' ' # to add between every value from the dictionary


if time[1] == ':':
    hours = int(time[0])
else:
    hours = int(time[0]+time[1])

while hours < 0 or hours > 24:
    time = input('Please re-enter the time: ')
    time = list(time)
    if time[1] == ':':
        hours = int(time[0])
    else:
        hours = int(time[0] + time[1])
while mychar not in 'abcdeghkmnopqrsuvwxyz@$&*=':
    mychar = input("Character not permitted! Try again: ")