#FINALS 2

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        else:
            print("One or both vertices not found in graph")
    
    def remove_edge(self,vertex1,vertex2):
          if vertex1 in self.adj_list and vertex2 in self.adj_list:
               self.adj_list[vertex1].remove(vertex2)
               self.adj_list[vertex2].remove(vertex1)
          else:
              print("One or both vertices not found in the graph")
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]
    
    def print(self):
        for vertex in self.adj_list:
            print(f"{vertex}:",end="")
            for neighbor in self.adj_list[vertex]:
                print(f" {neighbor} ",end="")
            print()


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
    





def bfs(g,start_vertex,target_vertex):
    visited = set()
    q = Queue()
    q.enqueue(start_vertex)
    visited.add(start_vertex)

    while not q.is_empty():
        current_vertex = q.dequeue()
        if current_vertex != target_vertex:
         print(current_vertex,end=" ")
         for neighbor in g.adj_list[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.enqueue(neighbor)
        else:
            print(f"{target_vertex}")
            break



names = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Eve",
    "Frank",
    "Grace",
    "Hank",
    "Ivy",
    "Jack",
    "Karen",
    "Leo",
    "Mona",
    "Nancy",
    "Oscar",
    "Paul"
]

graph = Graph()


for x in names:
    graph.add_vertex(x)





graph.add_edge('Alice', 'Bob')
graph.add_edge('Alice', 'Diana')
graph.add_edge('Alice', 'Eve')
graph.add_edge('Alice', 'Paul')

graph.add_edge('Bob', 'Charlie')
graph.add_edge('Bob', 'Grace')

graph.add_edge('Charlie', 'Eve')
graph.add_edge('Charlie', 'Frank')
graph.add_edge('Charlie', 'Hank')

graph.add_edge('Diana', 'Eve')
graph.add_edge('Diana', 'Ivy')

graph.add_edge('Eve', 'Frank')

graph.add_edge('Frank', 'Jack')

graph.add_edge('Grace', 'Hank')
graph.add_edge('Grace', 'Karen')

graph.add_edge('Hank', 'Ivy')
graph.add_edge('Hank', 'Leo')

graph.add_edge('Ivy', 'Jack')
graph.add_edge('Ivy', 'Mona')

graph.add_edge('Jack', 'Karen')
graph.add_edge('Jack', 'Nancy')

graph.add_edge('Karen', 'Leo')
graph.add_edge('Karen', 'Oscar')

graph.add_edge('Leo', 'Mona')
graph.add_edge('Leo', 'Paul')

graph.add_edge('Mona', 'Nancy')

graph.add_edge('Nancy', 'Oscar')

graph.add_edge('Oscar', 'Paul')









print("This is the social network: ")

graph.print()


print()
print("Enter the starting person",end=" ")
enter_user = input()
print("Enter the target person",end=" ")
end_user = input()

if enter_user and end_user not in names:
    print("ERROR")
else:
    bfs(graph,enter_user,end_user)