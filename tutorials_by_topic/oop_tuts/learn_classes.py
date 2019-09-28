class Person:
    """Person class returns basic attributes of a person"""

    num_of_people = 0
    
    # init is a constructor of the class where all the attributes are passed
    def __init__(self, firstname, lastname, age, email): # self is a instance variable as it refers to every instance of class which gets created
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.email = email
        Person.num_of_people = Person.num_of_people + 1


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)    


print("No. of People before: ", Person.num_of_people)

p1 = Person('jon', 'doe', '28', 'jon.doe@email.com')
p2 = Person('alice', 'wonderland', '18', 'alice.wondeland@email.com')
print(p1.firstname)
print(p1.fullname())
print(p2.email)

print("No. of People after: ", Person.num_of_people)

print(help(Person))