file = open('test.csv', 'r')
lines = file.readlines()
for i in range(1, len(lines)):
    lines[i] = lines[i].split(',')
    lines[i][1] = float(lines[i][1])
    lines[i][2] = int(lines[i][2])

print(lines)
lines = lines[1:]

A = 0
header = 0
average_gpa = 0
num_without_a_so_far = 0
for student in lines:
    if student[1] >= 90:
        A += 1

for i in range(len(lines) - 1, -1, -1):
    if lines[i][1] < 90:
        num_without_a_so_far += 1
        if num_without_a_so_far == 2:
            print(f'student name: {lines[i][0]}')
            break
print(A)
file.close()