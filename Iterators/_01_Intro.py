""" Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol,
 which consist of the methods __iter__() and __next__().0

 StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
"""

nums = [10, 11, 2, 3, 5, 76, 87]
print("nums is  :", nums)

for i in nums:
    print(i)

print("====================")

for i in range(len(nums)):
    print(nums[i])

print("=======================")

nums = iter(nums)
print(nums.__next__())
print(nums.__next__())
print(nums.__next__())
print(nums.__next__())
print(nums.__next__())

print("===============================")


# print 1 to 10


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()

print(next(values))
for i in values:
    print(i)

print("=====================================")


class TopFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


obj = TopFive()

for i in obj:
    print(i)

print("========================================")

list1 = [1, 2, 'hello']
print(iter(list1))  # <list_iterator object at 0x000001C98FB2C208>


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= self.end:
            val = self.value
            self.value += 1
            return val
        else:
            raise StopIteration


range = MyRange(1, 17)

for i in range:
    print(i)

print("=====================================")


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 18)

print(next(nums))

print("=====================================================")


print("============================================================")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)



print("======================================================")
iterable_value = 'kumar'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break



print("===============================================")

# Iterating over a list
print("List Iteration")
l = ["kumar", "yuvi", "kiran"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("kumar", "yuvi", "kiran")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "kumar"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i])) 
