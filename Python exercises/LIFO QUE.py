import queue

quelifo = queue.LifoQueue()

for x in range(4):
    quelifo.put(str(x))
    
#   Must be a while loop to empty out from the end !!! 
while not quelifo.empty():
       print(quelifo.get(x),end=' ')
    

    
