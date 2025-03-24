# def greet(name):
#     return "hello " + name

# greet("lasha")
# #hello lasha is written by return

#1
# https://www.codewars.com/kata/55685cd7ad70877c23000102
def make_negative(number):
    if number > 0:
        return -number
    return number

#2
# https://www.codewars.com/kata/5168bb5dfe9a00b126000018
def solution(word):
    solution = ""
    for i in range(len(word) - 1, -1, -1):
        solution += word[i]
    return solution

#3
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8
def number_to_string(num):
    return str(num)