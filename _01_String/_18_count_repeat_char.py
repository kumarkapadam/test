# count repeated characters in a string

'''
CRUD : Retrieval
state : string, dictionary
behaviour : for, if, in , +=, =

taking the string input from the user and initializing an empty dictionary
looping the given string and using condition adding key value pairs to the dictionary
and finally looping the dictionary to print the chars and count of repetition in the string

'''

s = str(input('enter a string:'))
d = {}

for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for j, k in d.items():
    print(j, ' : ', k)

s = str(input('enter a string:'))


def char_repeat_conut(string):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for j, k in d.items():
        print(j, ' : ', k)


char_repeat_conut(s)