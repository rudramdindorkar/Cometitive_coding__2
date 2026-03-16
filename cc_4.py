# for i in range (1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range (1,5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1, 6), range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i," ",j)

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# username = ''
# password = ''
# while username != "admin" and password != "hello":
#     username = input("Enter username :")
#     password = input("Enter password :") 

# n = int(input("Enter number:"))
# sum = 0
# i = 1
# while i <= n :
#     sum = sum + i
#     i = i + 1
# print("the sum of first ",n,"numbers is :",sum)

# code to  remove duplicate
# name = "prashant"
# result = ""

# for i in name:
#     if i not in result:
#         result += i
# print(name)
# print(result)

# reverse the string using loop
# name = "Prashant"
# rev = ""

# for char in name:
#     rev = char + rev 
# print(rev)

# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This my purchased cart item")
#         continue
#     print(i)

#palindrome
# n = "racecar"
# n = input("Enter:")
# if n == n[::-1]:
#     print("palindrome string")
# else:
#     print("not a palindrome string")

#anagrams are there same letter in 2 different words input:"listen" and "silent"  output anagrams

# w1 = input("Enter first word: ")
# w2 = input("Enter second word: ")

# if sorted(w1) == sorted(w2):
#     print("These are anagrams")
# else:
#     print("Not anagrams")

# Input :Dictionary:{"name":"Alice"},Key:"age",Value:30
#output : Dictionary:{"name":"Alice","age",30}

# dictionary = {"name": "Alice"}
# key = "age"
# value = 30

# dictionary[key] = value

# print(dictionary)

#remove key
# dictionary = {"name": "Alice", "age": 30}
# del dictionary["age"]
# print(dictionary)

#nested for loop
# for i in range(1,4):   #outer loop => row's
#     for j in range (1,4):  #inner loop =>col's
#         print(i, end=" ")
#     print()

# n = int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

# n = int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()