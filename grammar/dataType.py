#!/usr/bin/python3

# List
movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]

# insert Data to List
movies.insert(3, 1996)
movies.insert(2, 1995)
movies.insert(1, 1994)

print(movies)
print(movies[1])
print(len(movies))
print("\n")

movies.append("The King of Plant");
# add on tail
print(movies)
# remove from tail
print(movies.pop())
# contact another list
movies1 = ["m1", "m2"]
movies.extend(movies1)
print(movies)
print("\n")
# remove 
movies.remove("m1")
movies.insert(0, "0")
print(movies)

# for each
print("\nfor each")
for movie in movies:
    print(movie)
# List in List
list1 = [1, 2, 3]
list2 = [41, 42, 43, 44]
list1.append(list2)
print(list1);
print(list1[3][2])

# for each inner List

def print_inner_list(m_list):
    if(isinstance(m_list, list)):
        for m in m_list:
            print_inner_list(m)
    else:
        print(m_list)

print_inner_list(list1)
