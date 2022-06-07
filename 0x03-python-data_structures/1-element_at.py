#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        i += 1
    if idx < 0:
        return None
    elif idx >= i:
        return None
    else:
        return my_list[idx]
