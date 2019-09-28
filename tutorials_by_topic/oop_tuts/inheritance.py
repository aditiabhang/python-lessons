# courtesy: https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/4-Inheritance/oop-finish.py

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # super() keyword is used to inherit the init vars of Employee class
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()


# Printing the Manager Class will show all it's inheritance info
print(help(Manager))

# class Manager(Employee)
#  |  Method resolution order:
#  |      Manager
#  |      Employee
#  |      builtins.object
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, first, last, pay, employees=None)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  add_emp(self, emp)
#  |  
#  |  print_emps(self)
#  |  
#  |  remove_emp(self, emp)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Employee:
#  |  
#  |  apply_raise(self)
#  |  
#  |  fullname(self)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Employee:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Employee:
#  |  
#  |  raise_amt = 1.04