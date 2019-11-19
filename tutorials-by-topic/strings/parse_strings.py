
'''
The startswith() and endswith() methods provide a very convenient way to perform basic prefix and suffix checking. 
Similar operations can be performed with slices, but are far less elegant.
'''

'''
Problem
You need to check the start or end of a string for specific text patterns, such as filename extensions, URL schemes, and so on.
'''

'''
A simple way to check the beginning or end of a string is to use the str.startswith() or str.endswith() methods.
'''

# example 1: Matching Text at the Start or End of a String

filename = 'spam.txt'

print(filename.endswith('.txt'))

print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))


# example 2:

'''
this is one part of Python where a tuple is actually required as input. 
If you happen to have the choices specified in a list or set, just make sure you convert them using tuple() first.
'''

choices = ['http:', 'ftp:']
url = 'http://www.python.org'

# url.startswith(choices)  # Error
print(url.startswith(tuple(choices)))


# example 3: 

filenames = ['one.c', 'two.h', 'three.txt', 'four.sh', 'fun.py']

print([name for name in filenames if name.endswith(('.c', '.h', '.py')) ])

