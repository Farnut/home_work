"""Задание 1
Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y"""

# x = input(f'Enter integer value [x] : ')
# y = input(f'Enter integer value [y] : ')
# multiple = 0
# while x.isnumeric() == False and y.isnumeric() == False:
#     x = input(f'Enter integer value [x], not alphabet : ')
#     y = input(f'Enter integer value [y], not alphabet : ')
# x = int(x)
# y = int(y)
# multiple = x ** y
# print(f'{x} to the power of {y} is {multiple}')

'''Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.'''

# amount = 0
# for i in range(100, 999, 1):
#     number = i
#     n1 = number // 100
#     n2 = ((number) // 10) % 10
#     n3 = ((number) // 1) % 10
#     if n1 == n2  or n1 == n3 or n2 == n3:
#         amount = amount + 1
# print(f'Total {amount} integers with two identical digits')

'''Задание 3
Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.'''

# total = 0
# for n in range(10, 10000, 1):
#     s = str(n)
#     if len(s) == 4:
#         if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[1] != s[2] and s[1] != s[3] and s[2] != s[3]:
#             total = total + 1
#     if len(s) == 3:
#         if s[0] != s[1] and s[0] != s[2] and s[1] != s[2]:
#             total = total + 1
# print(f'Total numbers with different digits is {total}')

'''Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.'''

# n = '136' # str(input(f'Enter your namber : '))
# n_new = ''
# for number in n:
#     if number == '3' or number == '6':
#         continue
#     n_new = n_new + number
# n = int(n_new)
# print(n)