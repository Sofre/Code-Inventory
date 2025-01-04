#BREATH FIRST TRAVERSAL
import queue
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
                print(f" -{neighbor}- ",end="")
            print()

    
graph = Graph()

def bfs(g,start_vertex):
    visited = set()
    q = queue.Queue()
    q.put(start_vertex)
    visited.add(start_vertex)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex,end=" ")
        for neighbor in g.adj_list[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)



for x in range(5):
    graph.add_vertex(x)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)

graph.print()
print()
bfs(graph,0)