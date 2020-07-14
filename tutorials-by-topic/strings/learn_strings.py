greeting = "Hello Python"

# length of the string
print(len(greeting))

# position of each characer in the string using index
print(greeting[4])
print(greeting[0:5])
print(greeting[6:])

# lower and upper methods
print(greeting.lower())
print(greeting.upper())

# SWAPCASE method
string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())

# count the occurences of a character or a word inside a string
print(greeting.count('l')) # count = 2
print(greeting.count('o')) 
print(greeting.count('World'))  # if the word doesn't exist it will return count as 0 


# find method to find the index of certain elements of a string can be found 
print(greeting.find('l'))  # in this case it shows the first occurence of char 'l' at index 2
print(greeting.find('Python')) # index = 6
print(greeting.find('World')) # index = -1 since 'World' does not exists in the string

# replace method to replace word in a string
# NOTE: a new variable is required to store the replaced word
message = greeting.replace("Python", "World!")
print(message)


# format method (formatted string)
first_name = 'Jon'
last_name = 'Doe'
full_name = '{} {} is missing'.format(first_name, last_name)

print(full_name)


# new way of string formatting using fstrings
city = 'Austin'
zipcode = '78758'
state = f'{city.upper()} {zipcode}'
print(state)


# split function returns a returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression.
# str.split(separator, maxsplit)
'''
A helpful string method when working with strings is the .split method. 
This function or method returns a data container called a list that contains the words from the input string. 

The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". 
It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). 
If the sep argument is not provided, the default separator is whitespace.

True to its name, the maxsplit argument provides the maximum number of splits. 
The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. 
You can read more about these methods in the Python documentation too.
'''


# by default splits at space and outputs the string as a list 
fruit = 'geeks for geeks'
print(fruit.split())

# split at comma separated outputs the whole word as one single element of the list
fruit = 'geeks for geeks'
print(fruit.split(','))

# CONVERT STRING INTO A LIST
fruit = 'geeks:for:geeks'
print("string converted into a list: ", fruit.split(':'))


# The join(sequence) method joins elements and returns the combined string. 
# The join methods combines every element of the sequence.

# define strings                                                         
firstname = 'Bugs'
lastname = 'Bunny'

# define our sequence                                                    
sequence = (firstname,lastname)

# join into new string                                                   
looneytunes = ' '.join(sequence)
print(looneytunes)

# join a list of words
words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)


# The find() method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)



# traversing a string an printing it in a single line
# for i in greeting:
#     print(i, end = "")


