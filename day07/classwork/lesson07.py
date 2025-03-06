# inp = int(input("enter number: "))
# print(inp)

# for i in range(5):
#     print("hello")

# i = 0
# while i < 5:
#     print("hello")
#     i += 1

####################################################
#classworks:

# 1)შექმენით პროგრამა რომელიც მომხმარებელს მოთხოვს 
# რაიმე ტექსტს და შემდეგ რიცხვს. პროგრამამ უნდა 
# გამოიტანოს ამ ტექსტის შესაბამისი ასო რიცსვის მიხედვით

# text = input(enter text: )
print(input("enter text: ")[int(input("enter number: "))])

#2) შექმენით პროგრამა რომელსც 100 დან - 1მდე გამოაქვს რიცხვები.
print("classwork N2")
for i in range(100, 0, -1):
    print(i)

#3) შექმენით პროგრამა რომელიც 1-100 მდე გამოაქვს მხოლოდ კენტი რიცხვები
print("classwork N3")
for i in range(1, 101, 2):
    print(i)

#4) შექმენით პროგრამა რომელსაც ათ-ათობით გამოაქვს 250-500მდე რიცხვები
print("classwork N4")
for i in range(250, 501, 10):
    print(i)

# 5) შექმენით პროგრამა რომელშიც შემოაყვანინებთ მომხმარებელს რაიმე სიყვას 
# და თუ ეს სიტყვა იწყება "_"-ით მაშინ გამოიტანეთ True - თუ არა False
print("classwork N5")
word = input ("enter a word: ")

if word[0] == "_":
    print(True)
else:
    print(False)


print("classwork N5 without if")
x = input ("enter a word: ")
print (x[0] == "_")

# 6) შექმენით პროგრამა რომელიც მომხმარებელს ეკითხება რიცხვს და
# თუ ეს ტიცხვი ლუწია 10-ჯერ გამოუტანს "yes", ხოლო თუ ის კენტია "No'-ს
print("classwork N6")
num = int(input("enter some number: "))
if num % 2 == 0:
    for i in range(10):
        print("Yes")
else:
    print("No")