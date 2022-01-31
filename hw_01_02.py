'''Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
вывести само число. Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.'''
# a = 1
# b = 100
# if a != 1 or b != 100:
#     print("Enter correct value")
# else:
#     for i in range(a, b + 1):
#         if i % 3 == 0 and i % 5 == 0:
#                 print("Fizz Buzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#                 print("Buzz")
#         else:
#                 print(i)
'''Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой до седьмой включительно.'''
# for i in range(0, 8):
#     a = 2
#     a = a ** i
#     print(a, end=' ')
'''Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит длительность разговора и выбирает 
с какого на какой оператор он звонит. Вывести стоимость на экран.'''

'''Задание 4
Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%. Пользователь 
вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию
200$, вывести итоги на экран.'''
stock = 200
bonus = 200
percnt_1 = 0.03
percnt_2 = 0.05
percnt_3 = 0.08
man1 = "Manager 1"
man2 = "Manager 2"
man3 = "Manager 3"
man1_salary = 0
man2_salary = 0
man3_salary = 0
man_sale_1 = float(input(f"Enter Manager 1 sales : "))
man_sale_2 = float(input(f"Enter Manager 2 sales : "))
man_sale_3 = float(input(f"Enter Manager 3 sales : "))
if man_sale_1 < 500:
    man1_salary = stock + (man_sale_1 * percnt_1)
elif man_sale_1 >= 500 and man_sale_1 <= 1000:
    man1_salary = stock + (man_sale_1 * percnt_2)
elif man_sale_1 > 1000:
    man1_salary = stock + (man_sale_1 * percnt_3)
if man_sale_2 < 500:
    man2_salary = stock + (man_sale_2 * percnt_1)
elif man_sale_2 >= 500 and man_sale_2 <= 1000:
    man2_salary = stock + (man_sale_2 * percnt_2)
elif man_sale_2 > 1000:
    man2_salary = stock + (man_sale_2 * percnt_3)
if man_sale_3 < 500:
    man3_salary = stock + (man_sale_3 * percnt_1)
elif man_sale_3 >= 500 and man_sale_3 <= 1000:
    man3_salary = stock + (man_sale_3 * percnt_2)
elif man_sale_3 > 1000:
    man3_salary = stock + (man_sale_3 * percnt_3)
top = max(man_sale_1, man_sale_2, man_sale_3)
if top == man_sale_1:
    man1_salary = man1_salary + 200
    print(f"TOP is {man1} He gets a {bonus}$ bonus.")
elif top == man_sale_2:
    man2_salary = man2_salary + 200
    print(f"TOP is {man2} He gets a {bonus}$ bonus.")
elif top == man_sale_3:
    man3_salary = man3_salary + 200
    print(f"TOP is {man3}. He gets a {bonus}$ bonus.")
print(f"{man1} salary is {man1_salary}$")
print(f"{man2} salary is {man2_salary}$")
print(f"{man3} salary is {man3_salary}$")

