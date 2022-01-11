# largest number in a list
list1 = []
num = int(input("enter  how many  numbers do you want"))
for i in range(num):
    number  = int(input("enter any number:"))
    list1.append(number)
print("list1 is :",list1)
list1.sort()
print("sorted list is :", list1)
print("smallest number is :",list1[0])
print("highest number is  :", list1[-1])
print("highest number is :",list1[num-1])
print("second largest number is :", list1[num-2])