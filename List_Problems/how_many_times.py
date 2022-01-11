x=[]
num = int(input("how many elements :"))
for i in range(num):
    print("enter element :",end=" ")
    x.append(int(input()))
print("the list is :",x)

y = int(input("enter element to count :"))
c = 0
for i in x:
    if y==i:
        c+=1
print('{} is found {} times'.format(y,c))