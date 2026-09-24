from datetime import date


name = input("What is your name? ")
year = int(input("What year were you born? "))
month = int(input("What month were you born? (in numbers)"))
day = int(input("What day were you born? ")) 

birth = date(year, month, day)

def age_calculator(birth : date) -> int: 
    current_date = date.today()

    age = current_date.year - birth.year

    if (current_date.month, current_date.day) < (birth.month, birth.day):
        age -= 1 
    return  age

print(age_calculator(birth)) 