# def hello():
#     print('Hello World')
# hello()

# def hello_name (name):
#     print(f'Hello {name}')
# hello_name('Andrey')
# hello_name('Alex')
# hello_name('Ben')

'''Задание 1
Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't let the noise of others opinions drown out your own inner voice.”Steve Jobs'''

# def said():
#     print(f"\"Don\'t let the noise of others opinions \ndrown out your own inner voice.\"\nSteve Jobs")
# said()

'''Задание 2
Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.'''
# def odd(a, b):  # параметры функции
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             print(i)
#
#
# number1 = int(input("Enter number1 : "))
# number2 = int(input("Enter number2 : "))
# odd(number1, number2)
# odd(1, 8)
# odd(4, 77)
'''Задание 4
Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве параметров.'''

# def maxi(a,b,c,d):
#     if a >= b and a >= c and a >= d:
#         print(a)
#     if b >= a and b >= c and b >= d:
#         print(b)
#     if c >= a and c >= b and c >= d:
#         print(c)
#     if d >= a and d >= b and d >= c:
#         print(d)
# maxi(1,2,3,4)

'''Задание 3
Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа. Функция принимает в качестве 
параметра: длину линии, направление, символ.'''

# def line(length, direction, symbol):
#     s = ''
#     while length > 0:
#
#         if direction == 'horizontal':
#             s = s + symbol
#         elif direction == 'vertical':
#             s = s + '\n' + symbol
#         length = length - 1
#     print(s)

'''Задание 5
Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров'''
# def sum(a,b):
#     sum = 0
#     for i in  range(a, b+1):
#         sum = sum + i
#     return sum
#
# a = sum(10,20)
# print(a)

'''Задание 6
Напишите функцию, которая проверяет является ли число простым. Число передаётся в качестве параметра. Если число простое нужно 
вернуть из метода true, иначе false.'''

n = 137
s = ''
for i in range(2,n):
    if n % i == 0:
        s = 'NOT SIMPLE'
        break
if s != 'NOT SIMPLE':
    s = 'SIMPLE'
print(s)
def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True