"""Задание 1
Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом. Палиндром — слово или текст,
которое читается одинаково слева направо и справа налево. Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба."""

# w = 'А буду я у дуба'
# result_w = ''
# w = w.lower()
# for symb in w:
#     if symb != ' ':
#         result_w = result_w + symb
# revers_w = result_w[::-1]
# if result_w == revers_w:
#     print(f"It's palindrome.")
# else:
#     print(f"It's not palindrome.")

'''Задание 2
Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. 
Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный текст. '''

# s = "So close, no matter how far. Couldn't be much more from the heart. Forever trusting who we are. And nothing else matters"
# word = ['nothing', 'else', 'matters']
# s_old = list(s.split())
# s_lo = s.lower()
# s_new = list(s_lo.split())
# for i in range(len(s_new)):
#     for j in word:
#         if j in s_new[i]:
#            s_old[i] = s_new[i].title()
# print(' '.join(s_old))

'''Задание 3
Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.'''

# s = "So close, no matter how far? Couldn't be much more from the heart! Forever trusting who we are. And nothing else matters."
# spec = '!?.'
# total_sentens = 0
# for i in range(len(s)):
#     l = s[i]
#     for p in spec:
#         if l == p:
#             total_sentens = total_sentens + 1
# print(f'Amount sentense is {total_sentens}')








