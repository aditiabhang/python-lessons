# DRY = Don't Repeat Yourself

def simple_func():
    pass

# returns None
print(simple_func())

# optional parameter: name var is set to a default 
def hello_func(greeting, name='you'):
    return '{} {}'.format(greeting, name)
    

# if we don't enter the 2nd parameter value in the function it will be set to default
print(hello_func('Hi'))

# but, if we pass a parameter in the function it will override the default 'name' parameter
# NOTE: the sequence of passing the parameter to a function is important 
print(hello_func('Hi', 'Python'))



# what will be the answer
x = 3
y = 4

def add(a, b):
   result = x + y
   print(result)

add(10, 20)

