# print the index of the character in a string

'''
CRUD : Retrieve
state : string
behaviour : if , for, ==

taking the string and a char as user input and checking weather the char is present in string or not
if true then looping the string and using if condition when ever the char and loop string
matches printing the loop number which is index number of that char in string

'''

s = str(input('enter a string:'))
char = str(input('enter a char to know index:'))

if char in s:
    for i in range(len(s)):
        if char == s[i]:
            print('index numbers:', i)
else:
    print('char is not present in string')

s = str(input('enter a string:'))
char = str(input('enter a char to know index:'))


def index_char(st, c):
    if char in st:
        for i in range(len(st)):
            if char == st[i]:
                print('index numbers:', i)
    else:
        print('char is not present in string')

index_char(s, char)
