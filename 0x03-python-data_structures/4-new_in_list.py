#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #new_list = my_list
    for i in my_list:
        i += 1

    #new_list = my_list
    if idx < 0:
        return my_list
    elif idx > i - 1:
        return my_list
    else:
        n = my_list[idx]
        #new_list = my_list
        new_list[idx] = element 
        my_list[idx] = n
        #new_list[] = element
        return new_list
