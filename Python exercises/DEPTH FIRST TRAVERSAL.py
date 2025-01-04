class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def append(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop(len(self.items)-1)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def print(self):
        return print(self.items)
    
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


def dfs(graph,start_vertex):
    visited = set()
    s = Stack()
    s.append(start_vertex)

    print("DFS Traversal Order: ")
    while not s.is_empty():
        vertex = s.pop()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            for neighbor in graph.adj_list[vertex]:
                if neighbor not in visited:
                    s.append(neighbor)

g = Graph()

for node in range(5):
    g.add_vertex(node)

g.add_edge(0,3)
g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(2,3)
g.add_edge(2,4)

g.print()
print()
dfs(g,0)

