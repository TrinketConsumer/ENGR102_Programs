time = input('Enter the time: ')
clock_type =  int(input('Choose the clock type (12 or 24): '))
mychar = input('Enter your preferred character: ')
time = list(time)
hours = int(time[0] + time[1])
while hours < 1 or hours > 24:
    time = input('Please re-enter the time: ')
    time = list(time)
    if len(time) > 4:
        hours = int(time[0] + time[1])
    else:
        hours = int(time[0])

while mychar not in 'abcdeghkmnopqrsuvwxyz@$&*=':
    mychar = input("Character not permitted! Try Again: ")
