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



def build_graph(vertex, vertex1, vertex2):
   # AJDE BREEEEEE MOZOK SUM
    graph = Graph()

    if vertex in graph.adj_list:
            print("Vertex exist")
    else:
        graph.add_vertex(vertex)
        graph.add_vertex(vertex2)
        if vertex1 in graph.adj_list and vertex2 in graph.adj_list:
          print(f"Adding edge between {vertex1} and {vertex2}")
          graph.add_edge(vertex1, vertex2)
        else:
          print("One or both vertices for the edge are not in the graph.")
    






build_graph("A","A","D")
build_graph("A","A","B")
build_graph("A","A","E")
build_graph("B","B","A")
build_graph("B","B","C")
build_graph("B","B","A")
build_graph("C","C","B")
build_graph("C","C","E")
build_graph("C","C","F")
build_graph("D","D","A")
build_graph("D","D","E")
build_graph("E","E","A")
build_graph("E","E","C")
build_graph("E","E","D")
build_graph("E","E","F")
build_graph("F","F","E")
build_graph("F","F","C")
