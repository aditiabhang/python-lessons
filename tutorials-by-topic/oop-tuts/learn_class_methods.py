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

# class method is used to create an alternate constructor to create an object
    @classmethod
    def from_string(cls, p_str):
        firstname, lastname, age = p_str.split('-') 
        return cls(firstname, lastname, age)     


# p1 = Person('jon', 'doe', '28')
p2 = Person('alice', 'wonderland', '18')

p1_str = 'adam-smith-34'
p2_str = 'harry-potter-14'

new_person1 = Person.from_string(p2_str)

print(new_person1.firstname)
print(new_person1.age)

