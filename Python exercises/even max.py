def even_highest(x):
    new_list=[]  

    for counter in x:
        if(counter%2==0):
          new_list.append(counter)
         
    print(max(new_list))
          



list  = [10,2,3,4,8,11,22,25]
even_highest(list)
