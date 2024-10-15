


x = input("Enter the value of x:  ")
y = input("Enter the value of y:   ")

x= int(x)
y= int(y)

temp = x
x = y
y = temp

print(f"The value of x after swapping  {x}")
print(f"The value of y after swapping : {y}")

print("Swapping without temp variable")

x = x^y
y = x^y
x = x^y
x = x^y
y = x^y
x = x^y

print("x:", x)
print("y:", y)


def swap(x,y):
    return y,x




print("This is a swap with a function!")
print(x,y)
