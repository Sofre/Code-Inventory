import queue

que_empty = queue.Queue()
que_full  = queue.Queue()

for x in range(4):
    que_full.put(x)
    print(que_empty.empty())
    print(que_full.empty())    