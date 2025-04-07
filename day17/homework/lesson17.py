lst = [10, 20, 30, 40, 50]

def manual_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return None

print(manual_index(lst, 20))

def manual_len(lst):
    count = 0
    for i in lst:
        count += 1
    return count

print(manual_len(lst))

def manual_reverse(lst):
    length = len(lst)
    for i in range(int(length / 2)):
        var = lst[i]
        lst[i] = lst[length - 1 - i]
        lst[length - 1 - i] = var
        
manual_reverse(lst)
print(lst)