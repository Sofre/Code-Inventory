def gcd(m,n):
    while m%n != 0:
     old_m = m
     old_n = n
     m = old_n
     n = old_m % old_n
    return n
## Greates Common Divisor method


class Fraction:
## Constructor of class
## (self) is object
    def __init__(self,top,bottom):
        self.top = top
        self.bottom = bottom
## Dunder method for converting to string 
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)
## Dunder method for overriding basic add function to specfic needs!!! 
    def __add__(self,other):
        new_top = self.top*other.bottom + self.bottom*other.top
        new_bottom = self.bottom*other.bottom 
        common = gcd(new_top,new_bottom)
        ## Returns new function instance with new var
        return Fraction(new_top//common,new_bottom//common)
# Dunder method for overriding basic is_eqaull_to function to specific needs!!!
    def __eq__(self, value):
        first_number = self.top * value.bottom 
        second_number = value.top * self.bottom
        return first_number == second_number




first_fraction  = Fraction(2,5)
second_fraction = Fraction(1,5)
result = first_fraction + second_fraction
print(first_fraction == second_fraction)
print(result)