#4
# num = int(input("please enter some number but not more than 50: "))
# while num > 50:
#     num = int(input('number is more than 50, please input again: '))
# if num <= 50:
#     for i in range (1, 101):
#         if i % num == 0:
#             print(i)

#5
x1 = 4
y1 = 5
z1 = 6

while True:
    x2 = int(input("please enter first number:"))
    y2 = int(input("please enter first number:"))
    z2 = int(input("please enter first number:"))

    if x1 == x2 and y1 == y2 and z1 == z2:
        print("you guessed correctly!")
    else:
        print("sorry, incorrect!")
        break