# print the even numbers from a given list


# count and display the vowels of a given text
# P01. REQ : Find length of given string   ie., "Hello World"

'''
1. CRUD       -retrieve
2. STATE      - string / input()
3. BEHAVIOR   - + operator / for loop
'''
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics 80%
'''

'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

# 2. Algorithm  80%

print("--------2. Algorithm----------")
even = []


def even_list(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            even.append(i)
    print("even list is ", even)


num = int(input("enter any number :"))
even_list(num)


# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")

# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
