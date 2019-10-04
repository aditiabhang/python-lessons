# yield is keyword which is used in generators to store the result of a function

# generators have advantages over lists in terms of performance and reability of the function

# NOTE: Generator do not hold all the values in the memory
def square_numbers(nums):
    for i in nums:
        yield i*i  
      

# my_list = []
#     for i in nums:
#         my_list.append(i * i)
#     print(my_list)  


squared_nums = square_numbers([1,2,3,4,5])

 
# this will print generator object 
# print(squared_nums)

# to print out the result of the function we use next() method 
# which will print out one value at a time everytime we use the next() method  

# print(next(squared_nums))
# print(next(squared_nums))

# NOTE: Running print statement every single time is cumbersome and there is possibity of exhausting the list and erroring out
# therefore we run for loop on output of a generator


for num in squared_nums:
    print(num)
