# selection sort

"""


# ascending order
1.search the list find out the minimum value
2.min()
3.first value is min-val



list1 = [10,4,15,11,8,3,57]
print("list1 is :", list1)
min_val  = min(list1)
print("minimum value is :",min_val)

"""


list1 = [10,4,15,11,8,3,57]
print("list1 is ",list1)


for i in range(len(list1)):
    min_val = max(list1[i:])
    min_ind = list1.index(min_val)
    list1[0],list1[min_ind] = list1[min_ind],list1[0]

print(list1)



print("=======================================")


list1 = [56,0,2,2,6,0]
print("list1 is :",list1)

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val,i)
    if list1[i] != list1[min_ind]:
        list1[i],list1[min_ind] = list1[min_ind],list1[i]

print(list1)