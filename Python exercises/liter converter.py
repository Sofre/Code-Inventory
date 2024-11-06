def converter(liters):
     meter  = liters/1000

     print(int(meter))



user = input("Enter liters to convert: ")
user = int (user)
converter(user)