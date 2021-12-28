#to match the item in two dictionaries.

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

print(" *******************     2. Algorithm     ******************")

print(" *********   method1  ************")
dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}

for i in dict1:
    for j in dict2:
        if dict1[i] == dict2[j]:
            print("  key and value  both matches ", dict1[i])

print(" *********   method2  ************")

for (key, value) in set(dict1.items()) & set(dict2.items()):
    print('%s: %s is present in both dict1 and dict2' % (key, value))

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")

# set(aa.items()).intersection(set(bb.items()))

