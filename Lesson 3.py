# import math
# print(math.factorial(3))

# from math import *
# print(factorial(4))


# for i in range(1,11):
#     for j in range(1,11):
#         print (f"{i} * {j} =", i * j)


# i = 1
# j = 1
# while i <= 10:
#     while j <= 10:
#         print(f"{i} * {j} =", i * j)
#         j=j+1
#     i = i + 1
#     j=1

# def f(x,y):
#     print(x ** y)
#
# f(3,2)
# a = f(3,2)
# print(a)


# def f(x,y):
#     return x ** y
#
# a = f(3,2)
# print(a)


# def f():
#     pass
#
# b = f()
# print(b)

# x=100
# def g():
#     global x
#     x +=1
#     print(x)
#
# g()


# f = lambda x, y: 10 * x + y
# print(f(2,3))


# try:
#     a = int(input("შემოიყვანე მთელი რიცხვი: "))
# except:
#     print("ვერ გადრავქმნი მთელ რიცხვად!")



a = "5"
b = "65n"
m = "mm"

print(a.isdigit())
print(b.isdigit())  #თუ ყველა ციფრია სტრინგში, მხოლოდ მაგ შემთხვევაშია თრუ
print(b.isalpha())  #თუ ყველა ასოა სტრინგში, მხოლოდ მაგ შემთხვევაშია თრუ
print(m.isalpha())


# from random import choice
#
# archevani=['a', 'b', 'c', 'd']
# print(choice(archevani))



# def calculator():
#     operatorebi = ['+', '-', '*', '**', '/']
#
# j = True
# while j:
#     try:
#         num1 = float(input("შემოიყვანეთ რიცხვი: "))
#         num2 = float(input("შემოიყვანეთ მეორე რიცხვი: "))
#         j = False
#     except:
#         print("გთხოვთ, შემოიყვანოთ რიცხვი!")
#         j = True
#
#     i = True
#     while i:
#         op = input("შემოიყვანეთ ოპერატორი: ")
#         if op not in operatorebi:
#             print("თქვენს მიერ არჩეულ ოპერატორზე კალკულატორი არ მუშაობს, აირჩიეთ რომელიმე: +, -, /, *, ** ")
#         else:
#             i = False
#
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "**":
#         result = num1 ** num2
#     else:
#         if num2 == 0:
#             print("ნულზე გაყოფა არ შეიძლება!")
#         else:
#             result = num1 / num2
#
#     return f"{num1} {op} {num2} = {result}"
#
# print(calculator())