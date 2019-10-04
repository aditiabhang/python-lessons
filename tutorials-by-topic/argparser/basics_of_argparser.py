import argparse
import sys 
import logging



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

    parser = argparse.ArgumentParser()
    
    parser.add_argument('a', type=float,default=1.0, help="please enter the first operand")
    parser.add_argument('b', type=float, default=1.0, help="please enter the second operand")
    parser.add_argument('operation', type=str, default=1.0, help="please enter atleast one operation (add, subtract, multiply or divide)")

    args = parser.parse_args()
    sys.stdout.write(str(calculate(args.a, args.b, args.operation)))