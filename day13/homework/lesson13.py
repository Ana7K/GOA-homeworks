# 1
num1 = int(input("enter 3_digit number: "))

digit_sum = (num1 // 100) + ((num1 // 10) % 10) + (num1 % 10)

change_after_division_on_3 = num1 % digit_sum

print (change_after_division_on_3)

# 2
number = int(input("enter a number: "))

number = number + number % 2
# if number % 2 == 1:
#     number += 1

print (number)

# 3
num2 = int(input("enter any number: "))

if num2 % 2 == 0:
    num2 += 5
else:
    num2 *= 3

print (num2 % 5)

# 4
name = input("Enter a name: ")
surname = input("Enter a surname: ")
age = int(input("Enter age: "))
country = input("Enter a country name: ")

print(f'{name} {surname} is {age} years old and lives in {country}.')

# 5
# num = 2
# print("Hello " + str(num) + " world")
# print("Hello", num, "world")
# print(f'Hello {num} world')

# third print is the best option beacuse it's more readable
# and doesn't need neither concatenation nor convertation(num to str in this case)
