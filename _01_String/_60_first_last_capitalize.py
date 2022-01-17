# capitalize first and last letters of each word of a given string

'''
CRUD : Update
State : string
behaviour : for, string
'''

# mathematics
'''
take a input string 
after we can convert the title then using slicing operator
exit
'''
# built_in_function

print("-------- algorithm-----------")
str = input("enter any string:")
str1 = str.title()
print(str1)
result = ""

for word in str1.split():
    print(word)
    result += word[:-1] + word[-1].upper() + " "
print(result)


print("-------------using functions--------")

def first_last_upper(str):  # function defination

    str1 = str.title()
    print(str1)
    result = ""

    for word in str1.split():
        print(word)
        result += word[:-1] + word[-1].upper() + " "
    return result
str = input("enter any string:")
first_last_upper(str)                  # function calling