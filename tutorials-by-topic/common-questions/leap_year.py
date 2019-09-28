months = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]



def is_leap(year):
    """function returns if a year is a leap year or not."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "a Leap year"
    else:
        return "not a leap year"   


print("Is ",is_leap(2030))
      


