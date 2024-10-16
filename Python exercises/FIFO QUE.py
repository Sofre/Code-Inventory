import queue

que = queue.Queue()

for i in range(0,4):
    que.put(i)
    print(que.get(i),end='')
    