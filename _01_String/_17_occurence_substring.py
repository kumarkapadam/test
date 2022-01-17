# to count occurrences of a substring in a string

'''

CRUD : Retrieval
State : string, Int
Behaviour : for, if , + ,==, +=

Taking a string and sub string as input from user and initializing the occurrence value of substring to zero
Looping the string and comparing the substring with the string of the loop when returns true
increasing the occurrence value with 1
'''

string = str(input('enter your string:'))
substring = str(input('enter the substring:'))

occur = 0

for i in range(len(string) - 1):
    if substring[0] + substring[1] == string[i] + string[i + 1]:
        occur += 1

print('count of substring in a string is: ', occur)

s = str(input('enter your string:'))
ss = str(input('enter the substring:'))


def substring_occur(string, substring):
    occur = 0
    for i in range(len(string) - 1):
        if substring[0] + substring[1] == string[i] + string[i + 1]:
            occur += 1
    return occur


print('count of substring in a string is:', substring_occur(s, ss))
