# 1
# https://www.codewars.com/kata/57089707fe2d01529f00024a/train/python
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True
    
# 2
# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
def repeat_str(repeat, string):
    return repeat * string

# 3
# https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python
def cookie(x):
    if type(x) == str:
        name = "Zach"
    elif type(x) == int or type(x) == float:
        name = "Monica"
    else:
        name = "the dog"
    return "Who ate the last cookie? It was " + name + "!"

# 4
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
def century(year):
    return(year + 99) // 100

# 5
# https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python
def find_average(nums):
    return sum(nums) / len(nums)