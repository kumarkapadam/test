
# convert a string in a list
'''

CRUD: Update
state : string, list
behaviour : for, append, split

taking the string as input and using the for loop iterating one by one char and appending to an empty list
can be convert to list using built in method split
'''

# ----- algorithm -------
s = str(input('enter a string: '))
l = []

for i in s:
    l.append(i)
print(l)
# ----- built in -----
s = s.split()
print(s)