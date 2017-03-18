#!/usr/bin/python3

# data serios
import pickle

a = []
b = []
try:
    with open('sun.txt') as text_file:
        # back file head
        text_file.seek(0)
        
        for line in text_file:
            try:
                (name, text) = line.split(':', 1)
                text = text.strip()
                if name == 'A':
                    a.append(text)
                elif name == 'B':
                    b.append(text)
            except ValueError:
                pass
        
except IOError as err:
    print('File Not Found! err:' +  str(err))


# write data to file
try :
    # w(lcean file ) w+(clean file read and write)  a(append)
    out = open('/home/llx/Desktop/data.txt', 'w+')
    print('A', file = out)
    print(a, file = out)
    print('B', file = out)
    print(b, file = out)
except IOError as err:
    print('File Not Exists! err:' + str(err))
finally:
    if 'out' in locals():
        out.close()

# dump data
try:
    with open('/home/llx/Desktop/dump.pickle', 'wb') as save_data:
        pickle.dump(a, save_data)
except IOError as err:
    print('File Not Exists! err:' + str(err))
except pickle.PickleError as err:
    print('Pick Error! err:' + str(err))

try:
    with open('/home/llx/Desktop/dump.pickle', 'rb') as read_data:
        readdata = pickle.load(read_data)
        print(readdata)
except IOError as err:
    print('File Not Exists! err:' + str(err))
except pickle.PickleError as err:
    print('Pick Error! err:' + str(err))
# load data

