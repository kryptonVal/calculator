
def addition(first_number, second_number):
    operation_result = float(first_number) + float(second_number)
    return operation_result

def subtraction(first_number, second_number):
    operation_result = float(first_number) - float(second_number)
    return operation_result

def multiplication(first_number, second_number):
    operation_result = float(first_number) * float(second_number)
    return operation_result

def division(first_number, second_number):
    if second_number != 0:
        operation_result = float(first_number) / float(second_number)
        return operation_result
    else:
        print("Error: Division by zero")
        return None
