# To sort (ascending and descending) a dictionary by value

#1. sort dictionary by value Ascending
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
a = sorted(d.items(), key=lambda x: x[1])
print(a)




#2. Sort dictionary by value descending

d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)




#3 import operator


import operator

x = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)


# 4 import collection

import collections

d = {2: 3, 1: 89, 4: 5, 3: 0}

od = collections.OrderedDict(sorted(d.items()))

print(od)










import collections

d = {2: 3, 1: 89, 4: 5, 3: 0}
od = collections.OrderedDict(sorted(d.items()))
for k, v in od.items():
    print(k, v)





y = {100: 1, 90: 4, 99: 3, 92: 1, 101: 1}
n = sorted(y.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(n)