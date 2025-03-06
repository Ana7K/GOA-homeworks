# name1 = "lasha"
# name2 = "luka"
# name3 = "elene"
# name1 + " " + name2 + " " + name3

# print(f"{name1} {name2} {name3}")

# print("hello" [3])

# print("len", len("hello")) 
# print("len" + str(len("hello"))) #string length

################################################
#classworks

#1
# text = input("enter some word: ")
# reversed_string = ""
# index = len(text) - 1

# while index >= 0:
#     reversed_string += text[index]
#     index = index - 1

# print("reversed will be: ", reversed_string)

#2
# sum == 0
# for i in range (0, 101):
#     sum = sum + i
# print("sum is: ", sum)

#3
# word = input("enter three letter word: ")
# if len(word) != 3:
#     word = input("enter EXACTLY 3-letter word: ")
# is_palindrome = word[0] == word[2]
# print(is_palindrome)

#4
# for i in range (100, 300):
#     print (i*i)

#5
# for i in range (10):
#     print(i % 2 == 1) # to start with False

# for i in range (10):
#     print(i % 2 == 0) # to start with True

#6
# N = int(input("enter some number: "))
# root = 0
# while root * root < N:
#     root += 1
# if root * root == N:
#     print(N, "'s root is:", root)
# else:
#     print('false')