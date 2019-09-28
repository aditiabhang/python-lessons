"""
Sets are a type of collection. This means that like lists and tuples, you
can input different python types. 

Unlike lists and tuples they are unordered.
This means sets do not record element position. 

Sets only have unique elements.
This means there is only one of a particular element in a set.
"""

 # To create an empty set 
my_set = set()
print(my_set)

# NOTE: empty set cannot be created using "{}" because that convention is used to create an empty dictionary


a = set('abracadabra')
print(a) # only unique characters will get printed out

b = set([1, 2, 3, 4, 5, 6, 4, 6, 1, 3, 4, 4, 9])
print(b) # only unique numbers will get printed out

# add an element to the set
b.add('d') # NOTE: set can store multiple data types at once
b.add(10)
print(b)

# add multiple elements to a set
b.update([10, 11, 12, 14])
print(b)

# add values from one set can be added to another using update method
c = set()
d = {1, 6, 4, 5, 5, 6}
c.update(['q', 'p', 'r'], d)
print(c)

# NOTE: cannot remove multiple values from a set
# remove values from a set using remove method
d = {1, 6, 4, 5, 5, 6, 7, 8, 9}
d.remove(6)
print(d)

# remove values from a set using discard method
d.discard(8)
print(d)


set_1 = {1 ,2, "red", "red", "blue", "red"}

set_1.remove(1)

print(set_1)

print("red" in set_1)
print("sanket" in set_1)


# intersection of 2 sets (with common elements) keeping set1 as reference
set_1 = {1 ,2, "red", "red"}
set_2 = {"red", 6, "blue", "yellow"}

set_3 = set_1.intersection(set_2) # common elements are red, blue and 2
print("intersection of values in set1 and set2: ", set_3)

# set2 and set3 are going to give us intersection of values that are in set1 
# keeping set1 as reference and checking values from other set2 that are common with first set
set_4 = set_1.intersection(set_2, set_3)
print("intersection of values in set1 and set2 and set3: ", set_4)


# difference of value between sets1 and set2 
# keeping set1 as reference and checking values from other set2 that are not in first set
set_4 = set_1.difference(set_2)
print("difference of sets: ", set_4)

set_4 = set_1.difference(set_2, set_3)
print("difference of values in set1 and set2 and set3: ", set_4)

# NOTE: to get common values that are not in both sets use symmetric difference method
set_4 = set_1.symmetric_difference(set_2)
print("symmetric difference between set1 and set2: ", set_4)

# union of sets (adding sets)
set_4 = set_1.union(set_2)
print("union of set1 and set2: ", set_4)


"""
You can convert a list to a set by using the function set; this is called type-casting.
You simply use the list as the input to the function set.
"""
new_list = [1,2,43,545, 'red']

new_set = set(new_list)
print(new_set)
