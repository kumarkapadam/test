# swap comma and dot in a string

'''
CRUD : Update
State : int, string
behaviour : for, if , elif, ==

taking string input from user and initializing two variables with zero
looping the string and storing the index positions of ',' and '.' and
replacing the ',' with '.' and '.' with ','

'''

s = str(input('enter a string:'))
ls = 0
fs = 0

for i in range(len(s)):
    if s[i] == ',':
        fs = i
    elif s[i] == '.':
        ls = i
    else:
        pass
s = s[:fs] + '.' + s[fs + 1:]
s = s[:ls] + ',' + s[ls + 1:]

print('string after swapping:', s)

s = str(input('enter a string:'))


def swap_com_dot():
    ls = 0
    fs = 0
    for i in range(len(s)):
        if s[i] == ',':
            fs = i
        elif s[i] == '.':
            ls = i
        else:
            pass
    return fs, ls


s = s[:fs] + '.' + s[fs + 1:]
s = s[:ls] + ',' + s[ls + 1:]
print('string after swapping:', s)
