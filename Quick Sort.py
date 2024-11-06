import random

def search_engine(list):
    if len(list)<=1:
       return list
    
    pivot = list[-1]

    left = [x for x in list[:-1] if x<=pivot]
    right = [x for x in list[:-1] if x>pivot]
          
       
    return search_engine(left) + [pivot] + search_engine(right)







list = []
for i in range(10):
  list.append(random.randint(1,10))


print(list)
sorted = search_engine(list)
print(sorted)