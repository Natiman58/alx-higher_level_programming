#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            idx = 3
            return my_list[idx]
