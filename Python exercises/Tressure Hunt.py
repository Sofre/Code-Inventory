import random
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
    landmarks = [
    'Buckingham Palace', 'Westminster Abbey', 'Big Ben', 'London Eye',
    'Trafalgar Square', 'National Gallery', 'Covent Garden', 'British Museum',
    'St. Paul\'s Cathedral', 'Tower of London', 'Tower Bridge', 'The Shard',
    'Borough Market', 'London Bridge', 'St. James\'s Park'
]


    list_monumnets = []
    for x in landmarks:
        list_monumnets.append(x)

    id_for_list = random.randrange(0,len(list_monumnets)-1,1)
    targeted_node = list_monumnets.pop(id_for_list)

    visited = set()
    s = Stack()
    s.append(start_vertex)
    
    

    print(f"Tressure is hiddent at: {targeted_node}")
    print()
    print(f"Path to tressure from {start_vertex} ")
    while not s.is_empty():
           vertex = s.pop()
           if vertex != targeted_node:
             if vertex not in visited:
              print(vertex,end="-> ")
              visited.add(vertex)
              for neighbor in graph.adj_list[vertex]:
                if neighbor not in visited:
                    s.append(neighbor)
           else:
                print(f"{targeted_node}")
                break

london_graph = Graph()
#NODES
landmarks = [
    'Buckingham Palace', 'Westminster Abbey', 'Big Ben', 'London Eye',
    'Trafalgar Square', 'National Gallery', 'Covent Garden', 'British Museum',
    'St. Paul\'s Cathedral', 'Tower of London', 'Tower Bridge', 'The Shard',
    'Borough Market', 'London Bridge', 'St. James\'s Park'
]


for landmark in landmarks:
    london_graph.add_vertex(landmark)
#EDGES
connections = [
    ('Buckingham Palace', 'Westminster Abbey'),
    ('Buckingham Palace', 'St. James\'s Park'),
    ('Westminster Abbey', 'Big Ben'),
    ('Big Ben', 'London Eye'),
    ('London Eye', 'Trafalgar Square'),
    ('Trafalgar Square', 'National Gallery'),
    ('National Gallery', 'Covent Garden'),
    ('Covent Garden', 'British Museum'),
    ('British Museum', 'St. Paul\'s Cathedral'),
    ('St. Paul\'s Cathedral', 'Tower of London'),
    ('Tower of London', 'Tower Bridge'),
    ('Tower Bridge', 'The Shard'),
    ('The Shard', 'Borough Market'),
    ('Borough Market', 'London Bridge')
]

for vertex1, vertex2 in connections:
    london_graph.add_edge(vertex1, vertex2)

for printout in landmarks:
    print(f"-{printout}")

print()
print("Enter your landmark:",end=" " )
landmark_input  = input()

if landmark_input not in london_graph.adj_list:
    print("Not in supported")
else:
    
    dfs(london_graph,landmark_input)
