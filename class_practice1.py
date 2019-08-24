import datetime

class User:
    """
    User function that takes users fullname and returns first and last name
    and takes the birthday and returns users age in years
    """
    
    def __init__(self, full_name, birthday):
        self.fullname = full_name
        self.birthday = birthday  #yyyymmdd
      
        name_separation = self.fullname.split(" ")
        first_name = name_separation[0]
        last_name = name_separation[1]
    
    def age(self):
        """takes users birthdate and returns users age in years"""
        date_today = datetime.date.today()
        date_today = date_today.year
        dob = self.birthday
        birth_year = dob[0:4]
        birth_month = dob[4:6]
        birth_day = dob[6:8]
        age = date_today - int(birth_year)
        return age 
        
        
        
        
        
user1 = User("Jon Doe", "20011201")
print("Users age is: ", user1.age())
