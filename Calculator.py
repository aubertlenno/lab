def calculate():
    operation = int(input("Enter a operation that you want to execute\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n"))
    if operation == 1:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        value = number1 + number2
        print(value)
    elif operation == 2:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        value = number1 - number2
        print(value)
    elif operation == 3:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        value = number1 * number2
        print(value)
    elif operation == 4:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        value = number1 / number2
        print(value)
    elif operation == 5:
        number1 = int(input("Enter the first number: "))
        exponent = int(input("Enter the exponent: "))
        value = number1 ** exponent
        print()
    else:
        print("Command not detected")


condition = 'yes'

while condition == 'yes':
    calculate()
    condition = input('Do you want to do another calculation? (yes/no): ')

    if condition == 'no':
        print("Program stopped")
        break