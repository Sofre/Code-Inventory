index = -1
for i in range(5,50,1):
    
    index = index + 1
    if(i==25):
        print(f"Index of the number {i} is : {index}")
        break
    else:
        continue

    
space = ' '
print(space)
print(space)
print(space)



image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],    
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0], 
]
for i in image:
    for value in i:
        if value == 0:
            print(" ", end=" ")  
        else:
            print("*", end=" ")  
    print()


print(space)
print(space)
print(space)





for i in range(1,6):
    for value in range(i):
        if(value <= i):
            print("*",end=" ")
           
        else:
          print("",end=" ")
    print()     


for i in range(4,0,-1):
    for value in range(i):
        if(value <= i):
            print("*",end=" ")
           
        else:
          print("",end=" ")
    print()    




print()


   







for i in range (1,10):
    for number in range(i):
        
        if(number<i):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()    