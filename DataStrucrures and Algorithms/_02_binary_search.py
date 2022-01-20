def b_search(list1,key):
    low  = 0
    high = len(list1)-1
    Found = True
    while low <= high and not Found:
        mid = (low +high) //2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("key is Found")
    else:
        print("key is not found")









list1 = []
num = int(input("enter how many number do you want:::"))
for i in range(num):
    elem = int(input("enter any number:::"))
    list1.append(elem)
print("list1 is    :",list1)
list1.sort()
print("sorted list1 is :",list1)
key = int(input("enter any key::"))
b_search(list1,key)