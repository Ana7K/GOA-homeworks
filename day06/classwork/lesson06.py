# review of 4th hw
# word = input("enter some word: ")
# amount = 0
# for i in word:
#     if i == 'A':
#         print(i)
#         amount = amount + 1

# if amount == 0:
#     print("there's no A's in your word")

# calculating factorial
# num = int(input("enter some number: "))
# result = 1
# for i in range(1, num+1):
#     result = result * i
#     # print(i, "'s factorial is: ", result)
# print(i, "'s factorial is: ", result)

# word = input("enter something: ")
# res = ''
# for i in word:
#     res = i + res
#     print(res)

###################################################
#classworks

#1
# num = int(input("enter some number: "))
# count = 0
# # if num == 2:
# #     print('your number is prime')

# for i in range(2, num):
#     if num % i == 0 and count == 0:
#         print('your number is not prime')
#         count += 1
# if count == 0:
#     print('your number is prime')


##################################################
print("The password has to be over 8 characters and must contain 'A'!")

password = input("please input a password: ")
while len(password) < 8 or 'A' not in password:
    password = input ('please input a password again: ')
print('correct')