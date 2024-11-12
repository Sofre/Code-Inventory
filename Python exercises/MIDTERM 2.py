import random



def selection_sort(list):
    for traverser in range(len(list)):
        min_index = traverser  
        for dummy_absorber in range(traverser+1, len(list)):  
            if list[dummy_absorber] < list[min_index]:
                min_index = dummy_absorber  
      
        list[traverser], list[min_index] = list[min_index], list[traverser]

def binary_search(list,item):
   low = 0
   high = len(list) - 1
   found = False
   while low<=high and not found:
      mid = (high+low)//2
      if(list[mid]==item):
         return True
      else:
         if item<list[mid]:
            low = mid + 1
         else:
            high = mid - 1
   return False

list=[]
for i in range(10):
   list.append(random.randint(1,10))

print(list)
selection_sort(list)
print(list)
print(binary_search(list,9))

