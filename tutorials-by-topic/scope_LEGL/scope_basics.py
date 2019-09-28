# Courtesy : https://github.com/CoreyMSchafer/code_snippets/blob/master/Scope/scope.py

'''
LEGB
Local, Enclosing, Global, Built-in
'''

# global variable
for a in range(2):
    x = 'global {}'.format(a)

# enclosed function is a function inside a function
def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)