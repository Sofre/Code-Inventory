def search_engine(list,item):
    first = 0
    last = len(list) - 1
    found = False
    while first < last and not found:
        midpoint = (first+last)//2
        if(list[midpoint]==item):
                found=True
        else:
             if item<list[midpoint]:
                  last = midpoint-1
             else:
                  first = midpoint+1
    return found


test = [0,1,2,8,13,17,18,19,32,42]
print(search_engine(test,32))

#I KILL MY SELF TONIGHT :D
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    
  
    if low > high:
        return False

    mid = (low + high) // 2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)  
    else:
        return binary_search(lst, target, low, mid - 1)

test = [0,1,2,8,13,17,18,19,32,42]
print(binary_search(test,10))

