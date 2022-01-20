# single quotation
str = 'kumar'
print("name is ", str)
print("type is ", type(str))

# double quotation
str = "hello"
print(str)
print(type(str))  # <class 'str'>

# triple quotation

str = """Quickly send and receive WhatsApp messages right from your computer.
     WhatsApp. End-to-end encrypted.
     Quickly send and receive WhatsApp messages right from your computer.
     Quickly send and receive WhatsApp messages right from your computer.   
     WhatsApp Web. To use WhatsApp on your computer:
     Open WhatsApp on your phone; 
     Tap Menu or Settings and select Linked Devices"""
print(str)

#  1. capitalize() :: Returns a string where the first character is upper case.

print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello welcome to programming language'
print("Normal string            :", str1)
str1.capitalize()  # Hello world   10
print("String after capitalize  :", str1)
print("String after capitalize! :", str1.capitalize())  # print(10)
print("String after capitalize!!:", str1)
str2 = str1.capitalize()  # x = 10
print("String after capitalize!!!:", str2)  # print(x)

'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hello world'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
print("----Way 2--------")
str1 = 'hello world'
print("String     : ", str1)
str2 = str1.capitalize()  # x = 10
print("String     : ", str1)
print("String     : ", str2)  # print(x)

# 3 : Current string should get modified
print("----Way 3--------")
str1 = 'hello world'
print("String     : ", str1)
str1 = str1.capitalize()
print("String     : ", str1)

print("-------------------------------------------------------------------------------------")

# 2. center() : Returns a space-padded string with the original string centered to a total of width columns.
print("------------- 2. center() -----------------")

print("center() : returns center padded string with mentioned length")

str1 = 'hello world'
print("Normal string                                                :", str1)

print("String after center function with width 28 & fillchar as $   :", str1.center(28, '$'))
print("String after center function with width 24                   :", str1.center(24))
print("-------------------------------------------------------------------------------------")

# 3. count() : Counts how many times str occurs in string or in a substring of string.
str1 = 'hello world'
print("------------- 3. count() -----------------")
print('count() : Counts how many times str occurs in string or in a substring of string.')

print("Normal string                           :", str1)

print("Number of e's in the total string are   :", str1.count('e', 0, len(str1)))
print("Number of x's in the total string are   :", str1.count('x', 0, len(str1)))
print("-------------------------------------------------------------------------------------")

# 4. decode() : Decodes the string using the codec registered for encoding.
str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("------------- 4. decode() -----------------")
print('decode() : Decodes the string using the codec registered for encoding..')

print("Encoded string        :", str2)
print("Decoded string        :", str2.decode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")

# 5. encode() : Returns the encoded version of the string.
str1 = 'hello world'
print("------------- 5. encode() -----------------")
print('encode() : Returns the encoded version of the string.')

print("Normal  string        :", str1)
print("Encoded string        :", str1.encode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")

# 6. endswith() : returns true if end with mentioned suffix.
str1 = 'hello world'
print("------------- 6. endswith() -----------------")
print('endswith() : returns true if end with mentioned suffix.')

print("Normal string                           :", str1)

print("If the Normal String ends with pe or not:", str1.endswith("pe", 5, 12))
print("If the Normal String ends with ld or not:", str1.endswith("ld", 2, 8))
print("If the Normal String ends with ld or not:", str1.endswith("ld", 3, 12))
print("----------------------------------------------------------------------------------------")

print("========================================================================================================")

print("**********Python Program to Replace all Occurrences of ‘a’ with $ in a String ********")
string = input("Enter string:")
string = string.replace('a', '$')
string = string.replace('A', '$')
print("Modified string:")
print(string)

print("========================================")

print("******   Python Program to Remove the nth Index Character from a Non-Empty String   ******")


def remove(string, n):
    first = string[:n]
    last = string[n + 1:]
    return first + last


string = input("Enter the string:")
n = int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))

print("==========================================")

print(" ********     Python Program to Detect if Two Strings are Anagrams     *********")

s1 = input("Enter first string:")
s2 = input("Enter second string:")
if (sorted(s1) == sorted(s2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")

print("===========================================")

print(
    "****    Python Program to Form a New String where the First Character and the Last Character have been Exchanged ****")


def change(string):
    return string[-1:] + string[1:-1] + string[:1]


string = input("Enter string:")
print("Modified string:")
print(change(string))

print("===========================================")
print("****   Python Program to Count the Number of Vowels in a String  *****")
string = input("Enter string:")
vowels = 0
for i in string:
    if (
            i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
print("Number of vowels are:")
print(vowels)

print("==============================================")

print("*******   Python Program to Take in a String and Replace Every Blank Space with Hyphen ********")
string = input("Enter string:")
string = string.replace(' ', '-')
print("Modified string:")
print(string)
print("================================================")

print("**********   Python Program to Calculate the Length of a String Without Using a Library Function   *******")
string = input("Enter string:")
count = 0
for i in string:
    count = count + 1
print("Length of the string is:")
print(count)

print("===============================================")

print("********* Python Program to Remove the Characters of Odd Index Values in a String    ******")


def modify(string):
    final = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final


string = input("Enter string:")
print("Modified string is:")
print(modify(string))


print("=================================================")
print("*******  Python Program to Calculate the Number of Words and the Number of Characters Present in a String ****")


string=input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

print("===================================================")

print(" ********    Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions ***")
string1=input("Enter first string:")
string2=input("Enter second string:")
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)



print("=================================================")
print("****     Python Program to Count Number of Lowercase Characters in a String   ******")
string=input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)


print("==================================================")


print("****************   check string is palindrome or not ******************* ")

string = input("Enter string:")
if string == string[::-1]:
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

print("======================================================")

print("*******    Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String   ***")
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)

print("=======================================================")