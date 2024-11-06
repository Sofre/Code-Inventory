def sorting_engine(list):
    for last_num in range(len(list)-1,0,-1):
        for i in range(last_num):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    


test = [2,4,6,19,3]
sorting_engine(test)
print(test)
print(max(test))
print(min(test))