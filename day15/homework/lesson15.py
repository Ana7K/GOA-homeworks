# 1
# შექმენით list-ი შემდეგი მნიშვნელობებით: 
# [1,4,3,6,9,11,17,13,26,30], თქვენი დავალებაა 
# გამოიტანოთ ლუწი რიცხვების ჯამი და კენტი რიცხვების რაოდენობა
listOfNumbers = [1,4,3,6,9,11,17,13,26,30] 
sum = 0
count = 0
for i in listOfNumbers:
    if i % 2 == 0:
        sum += i
    else:
        count += 1
print("sum of even numbers: ", sum)
print("count of odd numbers: ", count)


# 2
# შექმნით list და ბოლოში ჩაამატეთ ნებისმიერი მნიშვნელობა
nums = [10,378,29,44,754,30]
nums.append(1000)
print(nums)


# 3
# მოცემული list-იდან: [1,2,3,3,4,5] ამოშალეთ ის რიცხვი რომელიც არღვევს თანმიმდევრობას
L = [1,2,3,3,4,5]
L.pop(3)
print(L)


# 4
# list-ში: [1,2,3,4,6,8,9] ჩაამატეთ ის ციფრები რომელიც არის გამოტოვებული
numbers = [1,2,3,4,6,8,9]
numbers.insert(0, 0)
numbers.insert(5, 5)
numbers.insert(7, 7)
print(numbers)


# 5
# კომენტარის სახით დაწერეთ რას აკეთებს append, pop, insert
# append will add an element at the end of a list.
# pop will take out whichever element you want by specifying the index.
# insert will add an element at any position in a list by specifying where(index) and what(value) you want to insert.