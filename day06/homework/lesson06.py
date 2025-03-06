#1
# num = int(input("enter some number: "))
# sum_of_odd_numbers = 0
# for i in range(1, num + 1, 2):
#     sum_of_odd_numbers += i
# print('sum of odd numbers is: ', sum_of_odd_numbers)

#2
# num = int(input("enter some number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

#3
# print("The password has to be over 8 characters and must contain 'A'!")
# password = input("please input a password: ")
# attempt = 3

# while attempt > 0 :
#     if len(password) >= 8 and 'A' in password:
#         print('correct password!')
#         break
#     else:
#         attempt -= 1
#         if attempt > 0:
#             password = input("wrong! please input a password again: ")
#         else:
#             print('no more attempts.')

#4
# text = input("enter some word: ")
# reversed_string = ""
# index = len(text) - 1

# for index in range(index, -1, -1):
#     reversed_string += text[index]

# print("reversed will be:", reversed_string)