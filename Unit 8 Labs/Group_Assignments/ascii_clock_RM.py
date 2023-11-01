time_list = list(time)
time1 = time.replace(':', '')
time1 = int(time1)
if time1 >= 1200 and clock_type == 12:
    if time1 >= 1300:
        if time1 >= 2200:
            time1 -= 1200
            time1 = str(time1)
            time1 = time1[:2] + ':' + time1[2:]
            time_list = list(time1)
            time_list.append('P')
            time_list.append('M')
        else:
            time1 -= 1200
            time1 = str(time1)
            time1 = time1[:1] + ':' + time1[1:]
            time_list = list(time1)
            time_list.append('P')
            time_list.append('M')
    else:
        time_list = list(time)
        time_list.append('P')
        time_list.append('M')
elif time1 < 1200 and clock_type == 12:
    time_list = list(time)
    if time_list[0] == '0':
        time1 += 1200
        time1 = str(time1)
        time1 = time1[:2] + ':' + time1[2:]
        time_list = list(time1)
        
    time_list.append('A')
    time_list.append('M')
else:
    time_list = list(time)