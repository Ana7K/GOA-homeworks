list1 = [6, 2]
list2 = [7, -10, 5]

# 1
def funct(list1, list2):
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)
    list3.sort()
    return list3
res = funct(list1, list2)
print(res)

# 2
def func(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return list1
    else:
        return list2
    
print(func(list1,list2))

# 3
def function(list1, list2):
    combined = list1 + list2
    counting_positives = 0
    sum_of_negatives = 0
    for i in combined:
        if i > 0:
            counting_positives += 1
        elif i < 0:
            sum_of_negatives += i
    return counting_positives, sum_of_negatives

print(function(list1,list2))

# 4
my_list = [2,18,7,3,6,0]
def no_divison_by3(my_list):
    result = []
    for i in my_list:
        if i % 3 != 0:
            result.append(i)
    return result

print(no_divison_by3(my_list))

# 5
def doubled(my_list):
    new_list =  []
    for i in my_list:
        i *= 2
        new_list.append(i)
    return new_list

print(doubled(my_list))