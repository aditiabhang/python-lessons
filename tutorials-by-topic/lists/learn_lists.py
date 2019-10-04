companies = ['IBM', 'Google', 'Apple', 'Microsoft', 'Amazon']

# basic slicing in a list
print(companies[0:3])
print(companies[3:])

# Using index method to find position of a element in the list 
print("Index of the element in the list: ", companies.index('Apple'))

# Using 'in' keyword to find if an element in a list or not. 
# It returns True or False 
# NOTE: useful in conditionals and looping through values
print('Google' in companies) 
print('Facebook' in companies) # False

# to add an element to the list
# append method adds element to the end of the list 
companies.append('Facebook')
print("Appended Company:", companies)

# if you want insert/add/append value anywhere in the list 
# use insert method
companies.insert(0, 'SpaceX')
# This shifts all the elements to the right after the element is inserted in between the list
print("Companies: ", companies)

# Extend method to insert elements from another list  to the end of the first list
companies2 = ['Tesla', 'Lexus']
companies.extend(companies2)
print(companies)

# remove elements from a list will pop off the last element from the list 
popped = companies.pop()
# will show us the popped element
print(popped)

print("Popped list:", companies)

# use remove method to remove specific element from the list 
removed = companies.remove('Facebook')
# will not show us the removed element.
# print(removed) # should show None
print(" using remove method: ", companies)

# Using sorted function: sorting the elements in a list 
# NOTE: sorted function creates a new list 
nums = [1, 4, 5, 3, 2]
new_nos = sorted(nums)
print("new sorted list: ", new_nos)


# sort method can only be used on lists
# NOTE: sort method does not create a new copy of the list. The list gets altered by itself
# using sort method to sort elements in a list 
# s_companies = companies.sort()  # None this will return None
companies.sort()
print("sorted list: ", companies)

# reverse elements in a list using sort method
companies.sort(reverse=True)
print("rev sort list: ", companies)

# alternate method to sort elements in a reverse order in a list 
# using reverse method: to sort the elements in reverse order
nums = [1, 4, 5, 3, 2]
nums.reverse()
print("using reverse method, sort list: ", nums)
print("min number in list: ", min(nums))
print("max number in list: ", max(nums))
print("Addition of all elements in the list: ", sum(nums))


# CONVERT LISTS INTO A STRING
# space separated strings
companies_to_string = '-'.join(companies)
print("List converted into a string: ", companies_to_string)


# CONVERT BACK STRING INTO A LIST
# split function splits the string at the hypen into a list
original_list = companies_to_string.split('-')
print("back to the original list: ", original_list)


# creating empty list 
empty_list = []
# or
#empty_list = list()