#Dictionaries are mutable

students = {'name': 'Jon', 'age': 25, 'courses': ['Math', 'Comp Sci']}

print(students)

# accessing/reading the key
print(students['courses']) 
print(students['courses'][1])

# accessing key using get() method
print(students.get('name'))
print("Print Math: ", students.get('courses')[0])

# accessing a key that does not exists
print(students.get('phone', 'Key does not exists'))

# adding key-value element to the dictionary
students['phone'] = '123-456-7890'
print(students.get('phone', 'Key does not exists'))

# using "del" keyword to delete any specific element in dict
del students['phone']
print(students)

# using pop method to delete any specific element in dict
students.pop('age')
print(students)

# updating value of the existing element in the dict
students['name'] = 'Janice'
print(students)  # dict now gets updated

# using update() method to update multiple elements of a dict
students.update({'name': 'Alice', 'age' : 21, 'phone': '555-5555'})
print(students) # updated dict

# finding out number of elements in a dict
print(len(students))

# accessing keys in a dict
print(students.keys())

# accessing values in a dict
print(students.values())

# using items() method returns a LIST of TUPLES consisting of key-values 
print(students.items())


