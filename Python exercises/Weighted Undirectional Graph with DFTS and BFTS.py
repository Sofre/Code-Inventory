#WEIGHT UNDIRECTION GRAPH USING DFS ITEM AND BFS ITEM

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        self.adj_list[vertex] = []  # Initialize with an empty list for neighbors
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 and vertex2 in self.adj_list:
            self.adj_list[vertex1].append((vertex2, weight))
            self.adj_list[vertex2].append((vertex1, weight))  # For undirected graph
    
    def print(self):
        for vertex in self.adj_list:
            print(f"{vertex}:", end=" ")
            for neighbor, weight in self.adj_list[vertex]:
                print(f"({neighbor},{weight} km)", end=" ")
            print()  # Newline for each vertex


class Stack:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return self.list == []
    
    def push(self, item):
        self.list.append(item)
    
    def peek(self):
        return self.list[-1]
    
    def pop(self):
        return self.list.pop()
    
    def print(self):
        print(self.list)


class Queue:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return self.list == []
    
    def enqueue(self, item):
        self.list.append(item)
    
    def dequeue(self):
        return self.list.pop(0)  # Return and remove the first element
    
    def print(self):
        print(self.list)


def DepthFirstTraversalSearch(g, start_vertex, target_vertex):
    visited = set()
    s = Stack()
    s.push(start_vertex)
    
    print(f"DFS Traversal Order to Target: {target_vertex}")
    
    while not s.is_empty():
        vertex = s.pop()
        if vertex != target_vertex:
            if vertex not in visited:
                print(vertex, end="-> ")
                visited.add(vertex)
                for neighbor, _ in g.adj_list[vertex]:
                    if neighbor not in visited:
                        s.push(neighbor)
        else:
            print(f"{target_vertex}")
            break


def BreathFirstTraversalSearch(g, start_vertex, target_vertex):
    visited = set()
    q = Queue()
    q.enqueue(start_vertex)
    visited.add(start_vertex)
    
    print(f"BFS Traversal Order to Target: {target_vertex}")
    
    while not q.is_empty():
        current_vertex = q.dequeue()
        if current_vertex != target_vertex:
            print(current_vertex, end=" ")
            for neighbor, _ in g.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.enqueue(neighbor)
        else:
            print(f"{target_vertex}")
            break


# Example Usage
graph = Graph()
graph.add_vertex("Tokyo")
graph.add_vertex("Japan")
graph.add_edge("Tokyo", "Japan", 2000)
graph.print()

BreathFirstTraversalSearch(graph, "Japan", "Tokyo")
DepthFirstTraversalSearch(graph, "Japan", "Tokyo")
