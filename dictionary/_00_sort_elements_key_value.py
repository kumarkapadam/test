# sort the elements of dictionary based on key,value
dict = {10: 'red', 35: 'green', 15: 'blue', 25: 'white'}
print("normal dictionary :", dict)
print("dictionary keys:", dict.keys())
print("dictionary value:", dict.values())

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)


for key, value in dict.items():
    print(key, '-----', value)

c1 = sorted(dict.keys(), key=lambda t: t[0])
print("sorted c1 ", c1)

c2 = sorted(dict.values())
print("sorted c2:", c2)
