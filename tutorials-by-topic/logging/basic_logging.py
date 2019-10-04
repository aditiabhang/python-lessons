import logging 

logging.basicConfig(level=logging.INFO)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a/b 



logging.info(add(10,5))
logging.info(subtract(10,5))
logging.info(multiply(10,5))
logging.info(divide(10,5))

