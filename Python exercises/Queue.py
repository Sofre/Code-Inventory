import random
class Queue:
    def __init__(self):
         self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    

def hot_potato(name_list,num):
    que = Queue()

    for name in name_list:
        que.enqueue(name)

    while que.size()<1:
        for i in range(num):
            que.enqueue(que.dequeue)

        que.dequeue()
        
    return que.dequeue()

ranitem = random.randrange(1,10)
print(hot_potato(["Henry","Mary","Steven","Mercury","Han"],ranitem))
