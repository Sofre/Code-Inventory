class Fraction:
    def __init__(self,top,bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)


my_f = Fraction(3,5)     
print(my_f)