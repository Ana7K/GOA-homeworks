# 1
# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

# def repeat_str(repeat, string):
#     return string * repeat

# print(repeat_str(5, "Hello "))


# 2
# https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python

# def say_hello(name):
#     return "Hello, " + name

# print (say_hello("Mr. Spock"))


# 3
# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

# def rps(p1, p2):
#     if p1 == p2:
#         return ("Draw!")
#     elif p1 == "scissors" and p2 == "paper":
#         return ("Player 1 won!")
#     elif p1 == "rock" and p2 == "scissors":
#         return ("Player 1 won!")
#     elif p1 == "paper" and p2 == "rock":
#         return ("Player 1 won!")
#     else:
#         return ("Player 2 won!")

# print(rps("scissors", "paper"))  # Output: "Player 1 won!"
# print(rps("scissors", "rock"))   # Output: "Player 2 won!"
# print(rps("paper", "paper"))     # Output: "Draw!"


# 4
# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

# def get_grade(s1, s2, s3):
#     avg = (s1 + s2 + s3) / 3
#     if avg <= 100 and avg >= 90:
#         return 'A'
#     elif avg < 90 and avg >= 80:
#         return 'B'
#     elif avg < 80 and avg >= 70:
#         return 'C'
#     elif avg < 70 and avg >= 60:
#         return 'D'
#     return "F"
    
# print (get_grade(25, 35, 20))


# 5
# https://www.codewars.com/kata/583710ccaa6717322c000105/train/python

# def simple_multiplication(number) :
#     if number % 2 == 0:
#         return number * 8
#     return number * 9

# print (simple_multiplication(5))


# 6
# შექმენით ფუნქცია რომელსაც გადაეცემა ორი პარამეტრი name, lastname. 
# თქვენი დავალებაა გამოიტანოთ სახელის პირველი ასო, წერტილი და გვარი.

# def full_name (name, lastname):
#     return name[0] + "." + lastname

# print (full_name("john", "wick"))