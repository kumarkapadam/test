# count and display the vowels of a given text

'''

CRUD : retrieve
state : string, list, dictionary
behaviour : for, if, +=, = , in

taking string input from user and initialising a list with vowels and initialising an empty dictionary
looping the string and using if condition storing the vowels in dictionary and and increasing the count of
that vowel

'''

s = str(input('enter a string: '))
v = ['a', 'e', 'i', 'o', 'u']
d = {}

for i in range(len(s)):
    if s[i] in v:
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
print('the vowels in string and their count:', d)

s1 = str(input('enter a string: '))


def vowels_string(s):
    vl = ['a', 'e', 'i', 'o', 'u']
    di = {}
    for j in range(len(s)):
        if s[j] in vl:
            if s[j] in di:
                di[s[j]] += 1
            else:
                di[s[j]] = 1
    return di


print('the vowels in string and their count:',vowels_string(s1))
