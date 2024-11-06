def calculate_age(year_of_birth, current_year=None):
    if current_year is None:
        from datetime import datetime
        current_year = datetime.now().year
    age = current_year - year_of_birth
    return age


def age_greater(x):

    if x>50:
        print("You are getting old !")
    


year_of_birth = int(input("Enter your year of birth: "))
age = calculate_age(year_of_birth)
print(f"Your age is: {age}")
age_greater(age)