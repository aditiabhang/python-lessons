numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index     0, 1, 2, 3, 4, 5, 6, 7, 8, 9  
#-ve      -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:stop:step]

# accessing 1st 5 elements of the list
print(numbers[0:5])

# accessing the entire list
print(numbers[:])

# accessing the entire list from a set start point
print(numbers[2:])

# will print out from 1 to 7
print("negative access: ", numbers[1: -2])

# will print out from 0 to 8
print(numbers[:-1])


# step through a list 
# will print out every other element in this list 
print(numbers[::2])

# IMP reading the list in a reverse order
print("reversal of list: ", numbers[::-1])

# will print out every other element in this list in a reverse order
print(numbers[-2:1:-2])

