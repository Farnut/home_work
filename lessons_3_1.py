# gender = 'male'#female
# age = 13
# if gender == 'male':
#     if age < 18:
#         print('A boy')
#     else:
#         print('A man')
# elif gender == 'female':
#     if age < 18:
#         print('A girl')
#     else:
#         print('A woman')
# else:
#     if age < 18:
#         print('A child')
#     else:
#         print('An adult')

number1 = input("Enter number1 : ")
command = input("Enter command : ")
number2 = input("Enter number2 : ")
if type(number1) == type(1):
    if type(number2) == type(1):
        number1 = int(number1)
        number2 = int(number2)
        if command == '+':
            print(number1, command, number2, '=', number1 + number2)
        elif command == '-':
            print(number1, command, number2, '=', number1 - number2)
        elif command == '*':
            print(number1, command, number2, '=', number1 * number2)
        elif command == '/':
            if number2 != 0:
                print(number1, command, number2, '=', number1 / number2)  # PEP 8 Ctrl + Alt + L
            else:
                print('Zero division')
        else:
            print('Incorrect command')

    else:
        print('Number2 is not int')
else:
    print('Number1 is not int')

# number1 = 3
# command = '+'
# number2 = 7
# if command == '+':
#     print(number1,command,number2,'=',number1 + number2)
# elif command == '-':
#     print(number1,command,number2,'=',number1 - number2)
# elif command == '*':
#     print(number1,command,number2,'=',number1 * number2)
# elif command == '/':
#     if number1 != 0:
#         print(number1,command,number2,'=',number1 / number2)
#     else:
#         print('zero division')
# else:
#     print('incorrect command')




