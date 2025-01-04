# MAZE
import random
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
                print(f" {neighbor} ",end="")
            print()

    

def bfs(graph,start_vertex):
    visited = set()
    q = queue.Queue()
    q.put(start_vertex)
    visited.add(start_vertex)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex,end=" -> ")
        for neighbor in graph.adj_list[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_vertex("I")
g.add_vertex("K")
g.add_vertex("J")
g.add_vertex("L")
g.add_vertex("M")
g.add_vertex("N")

g.add_edge("A","B")
g.add_edge("B","C")
g.add_edge("C","D")
g.add_edge("C","G")
g.add_edge("D","E")
g.add_edge("E","F")
g.add_edge("G","H")
g.add_edge("H","K")
g.add_edge("H","I")
g.add_edge("I","J")
g.add_edge("K","L")
g.add_edge("L","M")
g.add_edge("M","N")

print()
g.print()

print()
print("\n\nBFS from A to N: ")
bfs(g,"A")
print()
print()
print()

#MATRIX 6x4
# var one is letters => list 
# var two is walls (NONE) => list
# random positioning 
# translate to graph data structure
# add walls and letters
# edge only letters (up,down,left,right) , design matrix edging 
# BFS from letter frist to last letter 
# if there is now way out , break 
# E N D




def bfs_matrix(graph, start_vertex):
    visited = set()
    q = queue.Queue()
    q.put(start_vertex)
    visited.add(start_vertex)

    reached_all_letters = False  
    found_letters = set()  

    while not q.empty():
        current_vertex = q.get()

       
        if current_vertex != "X":
            print(current_vertex, end=" -> ")

           
            if current_vertex not in ["X"]:
                found_letters.add(current_vertex)

           
            for neighbor in graph.adj_list.get(current_vertex, []):
                if neighbor not in visited and neighbor != "X":  
                    visited.add(neighbor)
                    q.put(neighbor)

    
    all_letters = [letter for letter in graph.adj_list.keys() if letter not in ["X"]]
    if set(all_letters) == found_letters:
        print("\nAll letters reached!")
    else:
        print("\nNo way out!")

def matrix(g):
    
    walls_list = []
    letters_list = []

    
    for letters in g.adj_list:
        letters_list.append(letters)

   
    for X in range(10):
        walls_list.append("X")

    
    matrix = []
    rows = 6
    cols = 4
    total_elements = rows * cols

    
    combined_list = letters_list + walls_list

    
    if len(combined_list) < total_elements:
        combined_list *= (total_elements // len(combined_list)) + 1

    combined_list = combined_list[:total_elements]

   
    random.shuffle(combined_list)

    
    for i in range(rows):
        row = combined_list[i * cols:(i + 1) * cols]
        matrix.append(row)

   
    print("\n\nRandom Matrix:")
    for row in matrix:
        print(" ".join(row))

   
    matrix_graph = Graph()

    
    for element in combined_list:
        matrix_graph.add_vertex(element)

  
    for i in range(rows):
        for j in range(cols):
            current_vertex = matrix[i][j]

          
            if current_vertex == "X":
                continue

                  
            if i > 0:  # UP EDGE  
                if matrix[i - 1][j]!= "X":
                    matrix_graph.add_edge(current_vertex, matrix[i - 1][j])
                
            if i < rows - 1: # DOWN EDGE
                if matrix[i + 1][j]!= "X":
                    matrix_graph.add_edge(current_vertex, matrix[i + 1][j])

            if j > 0:  # LEFT EDGE
                if matrix[i][j - 1] !="X": 
                    matrix_graph.add_edge(current_vertex, matrix[i][j - 1])

            if j < cols - 1:  # RIGHT EDGE
                if matrix[i][j + 1]!="X":
                    matrix_graph.add_edge(current_vertex, matrix[i][j + 1])

    
    print("\n\nPATH (BFS)")
    bfs_matrix(matrix_graph, "A")


matrix(g)