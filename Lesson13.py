#str Методы строк
#итерируемый тип данных / неизменяемый тип данных
# h = "Hello World"
# print(h)
# print(h[0])

# n = 'Yurii Alexandrovich Ukhin'
#     #0123456789
# print(n[6],n[11],n[12])# and
# print(n[13],n[14],n[15],n[8],n[2]) # rover
# print(n[0],n[14],n[1]) # you

'''Задание 1
Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите на экран.'''
# s = 'Hello World!'
# print(len(s))
# for i in range(len(s)):
#     print(s[i])
# s = 'Hello World!'
# for i in range(1,len(s)+1):
#     print(s[-i])

'''Задание 2
Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба количества на экран.'''
#V1
# letters = 'abcdefghijklmnopqrstuvxyz'
# numbers = '0123456789'
# s = 'hello123'
# count_numbers = 0
# count_letter = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letter = count_letter + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1

#V2
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)

'''Задание 3
Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается искомый символ. 
Полученное число выведите на экран.'''
s = 'Abrakadabra'
symbol = 'a'
count = 0
for l in range(len(s)):
    a = s[l]
    if a == symbol:
        count = count + 1
print(count)