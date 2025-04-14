#classwork

# 1
# https://www.codewars.com/kata/5834fec22fb0ba7d080000e8/discuss/python
def six_toast(num):
    return abs(num - 6)

# 2
list1 = [3,4,5]
list2 = [6,7,8]
list3 = []
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
print(list3)

# 3
lst = [1,2,3]
def remove_odds(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(remove_odds(lst))

# 4
def join_numbers(numbers):
    result = ""
    for i in numbers:
        result += str(i)
    return result
print(join_numbers(lst))

# 5
# https://www.codewars.com/kata/50ee6b0bdeab583673000025
a = "code"
b = "wa.rs"
name = a + b