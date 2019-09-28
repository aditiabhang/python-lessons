
class Person:
    """Person class returns basic attributes of a person"""

    num_of_people = 0
    
    # init is a constructor of the class where all the attributes are passed
    def __init__(self, firstname, lastname, age, ): # self is a instance variable as it refers to every instance of class which gets created
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        Person.num_of_people = Person.num_of_people + 1


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)  


    # Static method can be called without creating an object or instance. 
    # Simply create the method and call it directly. 
    # This is in a sense orthogonal to object orientated programming: we call a method without creating objects.

    @staticmethod
    def is_dancing():
        print("Person is Dancing")
 


# here we are using the static method on the Person class 
Person.is_dancing()

# for a regular method in a class we need to create an object
# for example
p2 = Person('alice', 'wonderland', '18')

print(p2.fullname())