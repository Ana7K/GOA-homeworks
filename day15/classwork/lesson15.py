# nums = [1,6,7,10,22,39,15]
# res = []
# for i in nums:
#     if i % 2 == 0:
#         res.append(i)
# print(res)


# nums = [1,5,2,29,21,13,61,27,101]
# res = []
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range (2, n):
#         if n % i == 0:
#             return False
#     return True

# for i in nums:
#     if isPrime(i):
#         res.append(i)
# print(res)


####################################################
#classwork

# 1
# შექმენით ფუნქცია, რომელსაც გადაეცემა შემდეგი ლისთი: 
# [1,23,165,2,3,92,10,34,911] და ერთი ინტეჯერი(მაგ. 3),
# თქვენი დავალებაა, რომ ახალ ცარიელ ლისთში შეინახოთ
# მხოლოდ ისეთი რიცხვები, რომლებიც უნაშთოდ იყოფიან 
# გადმოცემულ ინტეჯერზე(ამ შემთხვევაში 3-ზე).

# nums = [1,23,165,2,3,92,10,34,911]
# res = []
# def dividesBy3 (n):
#     if n % 3 == 0:
#         return True

# for i in nums:
#     if dividesBy3(i):
#         res.append(i)
# print(res)


# def cw1 (L, num):
#     res = []
#     for i in L:
#         if i % num == 0:
#             res.append(i)
#     return res

# print(cw1([1,23,165,2,3,92,10,34,911],3))


# 2
# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b

# def reverse_list(l):
#     reversed_list = []
#     for i in range(len(l)-1, -1, -1):
#         reversed_list.append(l[i])
#     return reversed_list

# print(reverse_list([1, 2, 3, 4]))


# other way
# def reverse_list(l):
#     reversed_list = []
#     for i in l:
#         res.insert(0,i)
#     return res


####################################################

# res = [1,2,4]
# res.pop(2)
# res.insert(1,3) #res.insert(index,value)
# print(res)

####################################################


# 3
# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

def even_last(numbers): 
    if not numbers:
        return 0
    sum = 0
    for i in range(0, len(numbers), 2):
        sum += numbers[i]
    
    return sum * numbers[-1]

print(even_last([1, 2, 3])) # (1+3)*3 = 12
print(even_last([]))