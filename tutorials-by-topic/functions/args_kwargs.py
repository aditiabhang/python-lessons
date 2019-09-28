
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# NOTE: any number of arguments can be passed as arguments when calling the student_info function
# return a list of args and a kwargs unpacks the dictionary of name and age (in this case)
student_info('Math', 'Art', name='Jon', age=18)


'''
alternatively, instead of passing the parameters in a function directly 
we can assign vars to store the parameters and then pass them to the function

example:
courses = ['math', 'art']
info = {name='Jon', age=18}

# NOTE: the vars will print out in the output only if we pass them in *args & **kwargs 
student_info(*courses, **info)
'''