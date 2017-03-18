#!/usr/bin/python3

try:
    # open file
    text_file = open('sun.txt')
    
    # back file head
    text_file.seek(0)
    
    for line in text_file:
        try:
            (name, text) = line.split(':', 1)
            print(name, end='')
            print('said:', end = '')
            print(text, end = '')
        except ValueError:
            pass
    
    # close opened file
    text_file.close();    
except IOError:
    print('File Not Found!')

