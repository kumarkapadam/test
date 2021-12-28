# count and display the vowels of a given text
# P01. REQ : Find length of given string   ie., "Hello World"

'''
1. CRUD       -retrieve
2. STATE      - string / input()
3. BEHAVIOR   - + operator / for loop
'''

# 0. Mathematics 80%
'''
1. Define the string, ant store the vowels in list ,and 
2. Take initial count as 0
3. Start reading it. 
4. While reading each char, increase the key count 
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

# 2. Algorithm  80%

print("--------2. Algorithm----------")
print(
    "********************** convert tuple to  list,set ***********************")

tup = (1, 2, 3, 4, 5)
print("type of tuple(tup) is :", type(tup))
print("normal tuple is       :", tup)

tup_to_list = list(tup)
print("tuple to list type    :", type(tup_to_list))
print("tuple to  list is     :", tup_to_list)

tup_to_set = set(tup)
print("tuple to set type    :", type(tup_to_set))
print("tuple to  set is     :", tup_to_set)

print(
    "********************** convert list to tuple,set ***********************")

list = [1, 2, 3, "kumar", 10.98]
print("type of list is           :", type(list))
print("list is                    :", list)

list_to_tup = tuple(list)
print("type of list_to_tuple is    :", type(list_to_tup))
print("list to tuple is            :", list_to_tup)

list_to_set = set(list)
print("type of list_to_set   is    :", type(list_to_set))
print("list to set is            :", list_to_set)

print("******************* convert set to list,tuple ***********************")

set1 = {1, 2, 3,4,5,6,7,8,9,100}
print(" type of set is     :", type(set1))
print(" set1  is           :", set1)

set_to_list  =  list(set)
print(type(set_to_list))   # TypeError: 'list' object is not callable  

set_to_tup = tuple(set)
print("type of set to tuple is  :",type(set_to_tup))
print("set to tuple is          :",set_to_tup)  #TypeError: 'type' object is not iterable """

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
