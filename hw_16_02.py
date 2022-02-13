"""Задание 1
Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в
указанном диапазоне, а также среднеарифметическое каждой группы."""

# a = 0
# b = 20
# sum_even = 0
# total_even = 0
# sum_odd = 0
# total_odd = 0
# sum_div_nine = 0
# total_div_nine = 0
# for n in range(a, b + 1, 1):
#     if n % 2 == 0:
#         sum_even = sum_even + n
#         total_even = total_even + 1
#         if n % 9 == 0:
#             sum_div_nine = sum_div_nine + n
#             total_div_nine = total_div_nine + 1
#     if n % 2 != 0:
#         sum_odd = sum_odd + n
#         total_odd = total_odd + 1
#         if n % 9 == 0:
#             sum_div_nine = sum_div_nine + n
#             total_div_nine = total_div_nine + 1
# arithmetic_even = sum_even / total_even
# arithmetic_odd = sum_odd / total_odd
# arithmetic_div_nine = sum_div_nine / total_div_nine
# print(f'Sum even {sum_even} \nArithmetic mean of even {arithmetic_even}')
# print(f'Sum odd {sum_odd} \nArithmetic mean of odd {arithmetic_odd}')
# print(f'Sum num div nine {sum_div_nine} \nArithmetic mean of num div nine {arithmetic_div_nine}')

'''Задание 2
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. Нужно отобразить на экране вертикальную 
линию из введенного символа, указанной длины. '''

# l = 5
# s = '%'
# sym = ''
# for n in range(l):
#     sym = s
#     print(s)

'''Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,если меньше 
нуля «Number is negative», если равно нулю «Number is equal to zero». Когда пользователь вводит число 7 программа 
прекращает свою работу и выводит на экран надпись «Good bye!»'''

# a = 1 #int(input(f'Enter your number : '))
# if a == 7:
#     print(f'Number {a} is a magic number! Good bye!')
# elif a > 0:
#     print(f'Number {a} is positive')
# elif a < 0:
#     print(f'Number {a} is negative')
# elif a == 0:
#     print(f'Number is equal to zero')

'''Задание 4
Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. Когда 
пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»'''

# a = 2
# b = 9
# summ = 0
# maxi = 0
# mini = 0
# while a == 7 or b == 7:
#     print(f'Number 7 is a magic number! Good bye!')
#     break
# else:
#     if a > b:
#         maxi = a
#         mini = b
#     elif a < b:
#         maxi = b
#         mini = a
#     summ = a + b
#     print(f'Sum is {summ}')
#     print(f'Max is {maxi}')
#     print(f'Min is {mini}')
