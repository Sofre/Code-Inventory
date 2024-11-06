def search_engine(list,item):
    pos = 0
    found = False
    while pos<len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos+=1
    return found

a_list = [1,2,3,4,5,6]
print(search_engine(a_list,2))






def search_engine(list,item):
    pos = 0
    positsion = []
    while pos<len(list):
        if list[pos] == item:
            positsion.append(pos)
            pos+=1
        elif list[pos]!=item:
            pos+=1
    
   
    
    if not positsion:
        return -1
    else:
        return positsion


a_list = ['a','b','c','b','m','n','n']
print(search_engine(a_list,'b'))
print(search_engine(a_list,'a'))
print(search_engine(a_list,'c'))
print(search_engine(a_list,'m'))
print(search_engine(a_list,'n'))
print(search_engine(a_list,'l'))
