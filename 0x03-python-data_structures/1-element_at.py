#!/usr/bin/pyhton3
def element_at(my_list, idx):
    b = len(my_list)

    if idx < 0:
        return None
    elif idx > b - 1:
        return None
    else:
        return my_list[idx]
