import numpy as np
import sys
counter = 0
file = open('module12quizF23.txt', 'r')
lines = file.readlines()
clean_list = []
for line in lines:
    line = line.strip()
    line = int(line)
    clean_list.append(line)

final_list = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
a = np.array(clean_list)
a.resize(100,100)
np.set_printoptions(threshold=sys.maxsize)
b = a[0:5, 85]
value_one = np.sum(b)
print(alpha[value_one])
c = a[4,:]
value_two = int(np.average(c))
print(alpha[value_two])
d = a[62, -5:]
value_three = np.sum(d)
print(alpha[value_three])
e = a[0]
value_four = np.min(e)
print(alpha[value_four])
f = a[29]
value_five = np.max(f)
print(alpha[value_five])
print()
message = 'zilhpzsyucavkzbf'
message2 = 'lbclllsnllnwoisu'
for i in message:
    num = alpha.index(i)
    counter += 1
    if counter == 1:
        final = num - value_one
        final_list.append(final)
    elif counter == 2:
        final = num - value_two
        final_list.append(final)
    elif counter == 3:
        final = num - value_three
        final_list.append(final)
    elif counter == 4:
        final = num - value_four
        final_list.append(final)
    elif counter == 5:
        final = num - value_five
        final_list.append(final)
        counter = 0
super_final = ''
for i in final_list:
    super_final += alpha[i]
print(super_final)
file.close()