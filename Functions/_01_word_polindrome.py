# P01 Req: given word is polindrome or not


#  Using Functions
print("-------- Using Functions----------")

'''
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->   if else == 
'''

print("*******     method1   **************")


def poly(str):
    if str == str[::-1]:
        print("string is palindrome")
    else:
        print("not palindrome")


string = input("enter any string:")
poly(string)

print("*******     method2   **************")

num = int(input("enter number:"))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")

print("*******     method-3   **************")

word = input("enter string:")
rev = ''.join(reversed(word))

if word == rev:
    print("palindrome")
else:
    print('not palindrome')


print("*******     method-4   **************")

word = input("enter string ")
rev = ''
for i in word:
    rev = i + rev
if rev == word:
    print("palindrome")
else:
    print("not palindrome")