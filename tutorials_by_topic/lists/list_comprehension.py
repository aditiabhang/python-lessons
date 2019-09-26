# append elements from one list to another empty list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using for loop
list1 = []
for n in list:
    list1.append(n)   # NOTE: list1 = list1.append(n) is not valid
print(list1[::-1])    # printing reverse


#### LIST COMPREHENSION ####

# squares of nos in list
my_list = [n*n for n in list]
print("squares of nos in list: ", my_list)

# return even nos from the list 

my_list = [n for n in list if n%2 == 0]
print("even nos:", my_list)

# return a tuple of (letter, number ) for each element of string 'abcd' and number '0123'
my_list = [(letter, number) for letter in 'abcd' for number in range(4)]
print("tuple pair list: ", my_list)


#### DICTIONARY COMPREHENSION ####

names = ['Peter', 'Tony', 'Wade', 'Bruce', 'Banner']
heros = ['Spiderman', 'Ironman', 'Deadpool', 'Batman', 'Hulk']

# NOTE: zip function packs elements from 2 lists into a tuple
# here we are packing elements of 2  lists into a dictionary
my_dict = {name:hero for name, hero in zip(names, heros)}
print("super heros: ", my_dict)


# if we want to remove one key-pair from our dictionary 
my_dict = {name:hero for name, hero in zip(names, heros) if name != 'Peter'}
print("super heros: ", my_dict)


#### SET COMPREHENSION ####
squares = [1, 4, 4, 9, 16, 16, 16, 25, 36, 36, 49, 49, 49, 64, 64, 64, 81, 100]

my_set = {n for n in squares}
print("set of numbers: ", my_set)