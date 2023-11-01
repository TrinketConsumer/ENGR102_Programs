print('')
for i in range(5):
    my_string = ''
    for input_time in time_list:
        if input_time != ':' and mychar != '' and input_time != 'A' and input_time != 'P' and input_time != 'M':
            dict_nums[input_time][i] = dict_nums[input_time][i].replace(input_time,mychar)
        if input_time != time_list[-1]:
            my_string += dict_nums[input_time][i] + space
        else:
            my_string += dict_nums[input_time][i]
    print(my_string)