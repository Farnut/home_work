'''Задание 1
Доработайте игру «Guess my number», добавив следующие функции.
■ Улучшите игру так, чтобы после угадывания числа,
выводился номер попытки, которую сделал пользователь для угадывания магического числа.
■ Улучшите игру так, чтобы после угадывания числа, выводилось количество потраченных попыток, которые сделал пользователь для
угадывания магическогочисла.
Задание 2
(Дополнительное, на высокую оценку)
Добавить возможность играть в игру заново. После того как пользователь угадает число, отображается сообщение:
«Вы хотите сыграть заново? ([Да] или [Нет])».Если пользователь отвечает [Да], игра начинается заново, если отвечает [Нет] – игра заканчивается'''

import random
game = True
money = 0
while game:
    secret_number = random.randint(1,3)
    contin = ''
    guess_number = 0
    lifes = 5
    attemp = 0  # переменная для кол-ва попыток
    while secret_number != guess_number and lifes > 0:
        guess_number = int(input("Enter number : "))
        lifes = lifes - 1
        attemp = attemp + 1 # счетчик попыток
        print(f'You have {lifes} lifes')
        if secret_number < guess_number:
            print(f'Your number greater than secret\nТвоё число больше, чем загаданное')
        elif secret_number > guess_number:
            print(f'Your number less than secret\nТвоё число меньше, чем загаданное')
    if lifes > 0:
        money = money + 5
        print(f'YOU WIN!!! \nYou used {attemp} tries')
        print(f'You guessed right on the {attemp} try')
        print(f'You have {money} money')
    else:
        print(f'YOU LOSE')
    new_game = str(input(f'Do you want to play again ? Print Yes [y] or No [n] : '))# вопрос о продолжении игры
    while new_game != 'y' and new_game != 'n':
        new_game = str(input(f'Enter correct answer : '))
    if new_game == 'y':
        game = True
    elif new_game == 'n':
        game = False