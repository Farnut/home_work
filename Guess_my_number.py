#Guess my number
# import random
# secret_number = random.randint(1,20)
# guess_number = 0
# while secret_number != guess_number:
#     guess_number = int(input("Enter number : "))
#     if secret_number < guess_number:
#         print('Your number greater than secret\nТвоё число больше, чем загаданное')
#     elif secret_number > guess_number:
#         print('Your number less than secret\nТвоё число меньше, чем загаданное')
# print('YOU WIN!!!')

# import random
# secret_number = random.randint(1,20)
# guess_number = 0
# lifes = 5
# while secret_number != guess_number and lifes > 0:
#     guess_number = int(input("Enter number : "))
#     lifes = lifes - 1
#     print(f'You have {lifes} lifes')
#     if secret_number < guess_number:
#         print('Your number greater than secret\nТвоё число больше, чем загаданное')
#     elif secret_number > guess_number:
#         print('Your number less than secret\nТвоё число меньше, чем загаданное')
# if lifes > 0:
#     print('YOU WIN!!!')
# else:
#     print('YOU LOSE')

# import random
# game = True
# money = 0
# while game:
#     secret_number = random.randint(1,20)
#     guess_number = 0
#     lifes = 5
#     while secret_number != guess_number and lifes > 0:
#         guess_number = int(input("Enter number : "))
#         lifes = lifes - 1
#         print(f'You have {lifes} lifes')
#         if secret_number < guess_number:
#             print('Your number greater than secret\nТвоё число больше, чем загаданное')
#         elif secret_number > guess_number:
#             print('Your number less than secret\nТвоё число меньше, чем загаданное')
#     if lifes > 0:
#         print('YOU WIN!!!')
#         money = money + 5
#     else:
#         print('YOU LOSE')
#     print(f'You have {money} money')