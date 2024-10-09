import math

first_side = input("Enter first side")
second_side = input("Enter second side")
third_side = input("Enter third side")

first_side = int(first_side)
second_side = int(second_side)
third_side = int(third_side)

s = (first_side+second_side+third_side)/2
s_inquaryformula = s*(s-first_side)*(s-second_side)*(s-third_side)
Area = math.sqrt(s_inquaryformula)

print(f"The area of the triangle is {Area}")
print(f"The area of the triangle is {round(Area)}")


