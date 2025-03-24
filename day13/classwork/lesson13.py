# მომხმარებელს შემოყავს სამნშნა რიცხვი. დათვალეთ და დაბეჭდეთ რა
# ნაშთს გვაძლევს შემოყვანილი რიცხვი მის ციფრთა ჯამზე გაყოფისას.
# მაგალითად, თუ მომხმარებელმა შემოიყვანა რიხვი 120, მისი ციფრთა
# ჯამია: 1 + 2 + 0 = 3. 120 ის ნაშთი 3 ზე გაყოფისას 0 ია. ამიტომ უნდა
# დაბეჭდოთ 0.

def res(num):
    x = 0
    for i in str(num):
        x += int(i)
    return num % x

print(res(340))

#other way:
num = 102
print(num % ((num // 100) + ((num // 10) % 10) + (num % 10)))

# classwork
# 1
# https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)