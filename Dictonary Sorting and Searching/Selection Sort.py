import random
def sort_engine(list):
    for outerr_loop in range(len(list)):
        min_index = outerr_loop
        for inner_loop in range(outerr_loop+1,len(list)):
            if list[inner_loop]<list[min_index]:
                min_index = inner_loop

            
        list[outerr_loop],list[min_index] =  list[min_index],list[outerr_loop]




list = []
for i in range(10):
    list.append(random.randint(1,10))
    

print(list)
sort_engine(list)
print(list)                                                                    