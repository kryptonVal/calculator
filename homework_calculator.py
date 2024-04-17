from mycalculator import (addition, subtraction, multiplication, division)

print("Hello! This is a simple calculator.")
print("It can make +, -, *, and / operations.")
continue_calculation = "y"


while continue_calculation == "y":
    first_number = (input("Enter first number: "))
    if first_number.isdigit():
        print("Yes. no is digit")
    else:
        exit()
    operator: str = input("+, -, *, /: ")
    second_number = (input("Enter second number: "))
    if second_number.isdigit():
        print("Yes. no is digit")
    else:
        exit()

    if operator == "+":
        operation_result = addition(first_number, second_number)
    elif operator == "-":
        operation_result = subtraction(first_number, second_number)
    elif operator == "*":
        operation_result = multiplication(first_number, second_number)
    elif operator == "/":
        operation_result = division(first_number, second_number)
    else:
        exit()

    operation_result = round(operation_result, 2)

    result = f"{first_number} {operator} {second_number} = {operation_result}"
    print(result)

    print("Do you want to calculate something else?")
    continue_calculation = input("y/n: ")
