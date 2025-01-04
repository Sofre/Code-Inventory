# Weighted graph

class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self,vertex1,vertex2,weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2,weight))
            self.adjacency_list[vertex2].append((vertex1,weight))
        else:
            print("One or both vertices not found in graph")
    
    def print(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: ",end=" ")
            for neighbor,weight in self.adjacency_list[vertex]:
                print(f"({neighbor},{weight})",end=" ")
            print()


g = WeightedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A","B",3)
g.add_edge("A","C",5)
g.add_edge("B","D",3)
g.add_edge("C","D",5)

g.print()
