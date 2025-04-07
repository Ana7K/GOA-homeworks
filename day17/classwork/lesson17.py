listn = [1,3,4,2,5]

print(sum(listn))
print(max(listn))
print(min(listn))
print(len(listn))

print(listn.count(2)) # "2" is in the list how many times
print(listn.index(2)) # "2's" index

listn.reverse()
print(listn)

listn.append(10)
print(listn)

listn.insert(2, 100)
print(listn)

listn.remove(100)
print(listn)

listn.pop(1)
print(listn)

listn.sort()
print(listn)

listn.copy()
print(listn)

listn.clear()
print(listn)

list1 = [1,2,3,4,5]
def manual_len(L):
    res = 0
    if type(L) == list:
        for i in L:
            res += 1
    else:
        for i in str(L):
            res += 1
    return res

print("length of the list is: ", manual_len(list1))

###############################################
# classwork

# 1
my_list = [1, 2, 3]

def manual_sum(my_list):
    total = 0
    for i in my_list:
        total += i
    return total

print("sum is: ", manual_sum(my_list))

# 2
my_2nd_list = [10, 2, 5]
def manual_append(my_2nd_list, val):
    new_list = []
    for i in my_2nd_list:
        new_list.append(i)
    new_list += [val]
    return new_list

print("0th way, My way:", manual_append(my_2nd_list, 7))

# 2 (1st Other way)
# def manual_append(L, x):
#     L.insert(len(L), x)
#     return L
# print("1st Other way:", manual_append(my_2nd_list, 8))

# 2 (2nd Other way)
def manual_append(L, x):
    res = []
    for i in L:
        res += [i]
    res += [x]
    return res
print("2nd Other way:", manual_append(my_2nd_list, 9))

# 2 (3rd Other way)
def manual_append(L, x):
    res = L.copy()
    res += [x]
    return res
print("3rd Other way:", manual_append(my_2nd_list, 10))

# 2 (4th Other way)
def manual_append(L, x):
    L += [x]
    return L
print("4th Other way:", manual_append(my_2nd_list, "a"))