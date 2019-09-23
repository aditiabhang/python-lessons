cars = ['Tesla', 'Toyota', 'Honda', 'Jeep', 'Ford']

# enumerate method returns both index and the actual element in a list 
# NOTE: we can choose what we want to use index or the actual element in the list 
for index, carname in enumerate(cars):
    print(index,carname)
    # print(carname)
    # print(index)

# Also, we can choose from which index we want to start the looping/enumeration
# we are starting to loop from index = 1 below
for index, carname in enumerate(cars, start=1):  
    print(index,carname)    