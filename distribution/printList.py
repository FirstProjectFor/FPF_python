#!/usr/bin/python3

"""
This is a function to iterator a list
"""

def print_inner_list(m_list, level = 0, flag = False):
   # This is a function to iterator a list

    if(isinstance(m_list, list)):
        for m in m_list:
            print_inner_list(m, level + 1, flag)
    else:
        if flag:
            for temp in range(level):
                print(" ", end = '')
        print(m_list)



