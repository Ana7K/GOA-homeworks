# name = 'Group65GGG'
# res = ''
# for i in name:
#     if i == 'G':
#         res = res + i
# print(res)


#######################################
#classworks

#1
# for i in range(2, 25):
#     if i % 2 != 0:
#         print(i)

#2
# name = input("enter your name: ")
# for i in name:
#     print(i)


########################################

# seats = 10
# while seats > 0:
#     print('seat sold')
#     seats = seats - 1

# print('\n')

# age = 10
# while age < 18:
#     print('you are a kid')
#     age += 1
# print('congrants, you are an adult')

########################################
#classworks

#3
correct_password = 'Ana123!'
password = input("enter your password: ")
while password != correct_password:
    password = input("incorrect! enter your password again: ")
print('password correct!')