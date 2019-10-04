# easiest and cleanest way to create a generator is using list comprehensions
# generators have advantages over lists in terms of performance 
 
my_nums = [1,2,3,4,5]
# NOTE: only difference is that the instead of '[]' brackets we use '()' brackets
squared_nums = (num * num for num in my_nums)

# this will print generator object
# NOTE: Generator do not hold all the values in the memory
print(squared_nums) 

for num in squared_nums:
    print(num)
