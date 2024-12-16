class Rectangle:
     
     def __init__(self,widith,height):
          self.widith = widith
          self.height = height 
        
          

     def __str__(self):
        return str(self.widith) + "," + str(self.height)
     

     def area(self):
         return self.height * self.widith
          
      
rect = Rectangle(3,5)
print(f"Rectangle details: {rect}") 
print(f"The area of the rectangle with {rect} is {rect.area()}")  