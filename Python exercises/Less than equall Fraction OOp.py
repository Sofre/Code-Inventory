

class Fraction:
    def __init__(self,top,bottom):
        self.top = top
        self.bottom = bottom

    
    def __str__(self):
        return self.top + "/" + self.bottom
    

    def __le__(self,value):
        first_number = self.top * value.bottom 
        second_number = value.top * self.bottom
        return first_number <= second_number
    


x = Fraction(1,4)
y = Fraction(1,2)
print(x<=y)