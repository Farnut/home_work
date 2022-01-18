##Sum&Multi
# number1 = float(input("Enter number 1 : "))
# number2 = float(input("Enter number 2 : "))
# number3 = float(input("Enter number 3 : "))
# comand = input("Enter command + or * : ")
# if comand == '+':
#     print(number1 + number2 + number3)
# elif comand == '*':
#     print(number1 * number2 * number3)
# else:
#     print("Incorrect comand")

##Max&Min&Medium
number1 = float(input("Enter number 1 : "))
number2 = float(input("Enter number 2 : "))
number3 = float(input("Enter number 3 : "))
comand = input("Enter command max or min or mid : ")
if comand == 'max':
    if (number1 > number2 > number3):
        print(number1)
    elif (number2 > number3 > number2):
        print(number2)
    else:
        print(number3)
if comand == 'min':
    if (number1 < number2 < number3):
        print(number1)
    elif (number2 < number3 < number1):
        print(number2)
    else:
        print(number3)
if comand == 'mid':
    print((number1 + number2 + number3)/2)
else:
    print("Wrong comand")

