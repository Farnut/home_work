'''Задание 1
Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y'''

# x = int(input(f'Enter integer value [x] :'))
# y = int(input(f'Enter integer value [y] :'))
# x = x ** y
# print(f'Your result is {x}')

'''Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.'''

# amount = 0
# for i in range(100, 1000, 1):
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
# for n in range(9990, 9999, 1):
#     s = str(n)
#     if s[0] != s[1] or s[0] != s[2] or s[0] != s[3] or s[1] != s[2] or s[1] != s[3] or s[2] != s[3]:
#         total = total + 1
# print(total)

'''Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.'''

a = 136
b = str(a)
for i in  range(len(b)):
    if b[i] == 3 or b[i] == 6:
        del b[i]
print(b)
