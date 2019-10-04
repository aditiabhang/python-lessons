def calculate(a, b, operation):

    """
    Calculate function calculates operations like add, subtract, multiply & divide on 2 operands

    For example: 
    To add 2 numbers: calculate(10, 5, "add")
    """

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b 
    elif operation == 'multiply':
        return a * b 
    elif operation ==  'divide':
        return a / b 


if __name__ == '__main__':

    print(calculate(10, 5, 'add'))
