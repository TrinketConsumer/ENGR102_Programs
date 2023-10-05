def myfun(num):
    count = 0
    for i in range(num,100):
        if 100 % num == 0:
            count += 1
            print(num, end = ' ')
            num += 1
        else:
            num += 1
            continue
    return count