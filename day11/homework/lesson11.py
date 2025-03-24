# 1
# https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python

def calculator(x, y, op):
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            if y == 0:
                return "can't be divided by 0"
            return x / y
    else:
        return "unknown value"
    
print (calculator(3, 0, '*'))

# 2
# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

def string_clean(s):
    """
    Function will return the cleaned string
    """
    cleaned_string = ""
    digits = "0123456789"
    
    for i in s:
        if i not in digits:
            cleaned_string += i
            
    return cleaned_string

print(string_clean("! !"))                 # Output: "! !"
print(string_clean("123456789"))           # Output: ""
print(string_clean("This looks5 grea8t!")) # Output: "This looks great!"


# 3
# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

# haven't covered lists yet

# 4
# https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

def count_char_occurrences(strng, char):
    count = 0
    
    for i in strng:
        if i == char:
            count += 1
            
    return count

print(count_char_occurrences("hello", "l"))
print(count_char_occurrences("bye", "a"))

# 5
# sololearn