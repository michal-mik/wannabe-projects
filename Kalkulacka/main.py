import math

def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return pow(a, b)

def square_root(a, b):
    return a ** (1/b)

print('---3Head CaLcUlAtOr---')
print('Addition [+]')
print('Subtract [-]')
print('Multiply [*]')
print('Divide [/]')
print('Power [**]')
print('N root [//]')




while True:
    choice = input(print('Choose from options:'))

    if choice in ('+', '-', '*', '/', '**', '//'):
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Wrong input')
            continue

        if choice == '+':
            print(num1, '+', num2, '=', addition(num1, num2))

        elif choice == '-':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '*':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '/':
            print(num1, '/', num2, '=', divide(num1, num2))

        elif choice == '**':
            print(num1, '˄', num2, '=', power(num1, num2))

        elif choice == '//':
            print(num2, 'v--', num1, '=', square_root(num1, num2))

        next = input("Do you want to continue? (y/n): ")
        if next == 'n':
            break

    else:
        print('Wrong input')