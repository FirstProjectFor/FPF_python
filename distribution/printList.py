#!/usr/bin/python3

"""
This is a function to iterator a list
"""

def print_inner_list(m_list):
    """
    This is a function to iterator a list
    """
    if(isinstance(m_list, list)):
        for m in m_list:
            print_inner_list(m)
    else:
        print(m_list)



