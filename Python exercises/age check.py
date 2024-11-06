def age_check(x):
    if x >=18:
        print("Congratulations! You can legally drive! ")
    else:
        print("Nope, you're DENIED! ")


def birthyear(x):
    return 2024 - x


age = input("Please enter your age: ")
age = int(age)
age_check(age)
birth = input("Please enter your year of birth: ")
birth = int(birth)
print(birthyear(birth))
