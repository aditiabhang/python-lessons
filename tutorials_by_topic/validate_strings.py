"""
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
"""

# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print("abc123".isalnum()) #True

# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
print("ABc@!".isalpha()) #False
print("XyZ".isalpha()) #True


# This method checks if all the characters of a string are digits (0-9).
print('123'.isdigit())


# This method checks if all the characters of a string are lowercase characters (a-z).
print ('abcd123#'.islower())
print('Abcd123#'.islower())


# This method checks if all the characters of a string are uppercase characters (A-Z).
print('ABCD123#'.isupper())
print('Abcd123#'.isupper())





