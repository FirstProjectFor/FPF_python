#!/usr/bin/python3

# use Set

# read data from file
def readDataFromFile(file):
   
    data = []
    try:
        with open(file) as dataFile:
            for line in dataFile:
                if ':' in line:
                    print(line)
                    data.extend(line.strip().split(':'))
    except IOError as err:
        print('Open file Error, file :' + file + str(err))
    return data

# call function
fileData = readDataFromFile('sun.txt')

print(fileData)

# sort and remove repeat Data
fileData = sorted(set(fileData))
print(fileData)

# handel arr data
lengthData = [len(data) for data in fileData]
print(lengthData)










