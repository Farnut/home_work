##AND , OR , NOT
# a = 2
# b = 3
# c = 4
# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)
#
# a = 12
# b = 6
# c = 4
# if a >= b >= c:
#     print(a)
#     if b >= c:
#         print(b)
#         print(c)
#     else:
#         print(c)
#         print(b)
# elif b >= a >= c:
#     print(a)
#     if b >= c:
#         print(b)
#         print(c)
#     else:
#         print(c)
#         print(b)

# x = int(input("Enter x : "))
# y = int(input("Enter y : "))
#
# if x > 0:
#     if y > 0:
#         print("I axis")
#     elif y == 0:
#         print("X axis")
#     else:
#         print("IV axis")
# if x == 0:
#     if y == 0:
#         print("ZERO")
#     else:
#         print("Y axis")
# if x < 0:
#     if y > 0:
#         print("II axis")
#     elif y == 0:
#         print("X axis")
#     else:
#         print("III axis")

# x = 4
# y = 0
# if x > 0 and y > 0:
#     print('I')
# elif x > 0 and y < 0:
#     print('IV')
# elif x < 0 and y < 0:
#     print('III')
# elif x < 0 and y > 0:
#     print('II')
# # elif x != 0 and y == 0:
# #     print('On Axis X')
# elif x > 0 and y == 0:
#     print('On Axis X+')
# elif x < 0 and y == 0:
#     print('On Axis X-')
# # elif x == 0 and y != 0:
# #     print('On Axis Y')
# elif y > 0 and x == 0:
#     print('On Axis Y+')
# elif y < 0 and x == 0:
#     print('On Axis Y-')
# elif y == 0 and x == 0:
#     print('ZERO')

# number = int(input("Enter number : "))
# if number % 2 == 0:
#     print('Even')
# elif number % 2 != 0:
#     print('Odd')
# else:
#     print('Zero')

'''Задание 2
Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно
требуется вывести на экран число и надпись Number is
multiple 7. Если число не кратно выведите на экран число
и надпись Number is not multiple 7.'''
number = int(input("Enter number : "))
if number == 0:
    print("Enter more then 0")
elif number %7 == 0:
    print("Number is multiple 7")
else:
    print("Number is not multiple 7")