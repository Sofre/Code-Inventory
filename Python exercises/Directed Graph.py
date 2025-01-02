class Node:
   
    def __init__(self,data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    

    def set_data(self,new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next = new_next


    
class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self,item):

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    # Lenght method
    def size(self):
        current = self.head
        count = 0
        while current !=None : 
            count += 1
            current = current.get_next()
        return count
    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == item:
                if previous is None:  
                    
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("")
    


class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()

    def add_directed_edge(self,vertex1,vertex_it_points_to):
        if vertex1 in self.adj_list and vertex_it_points_to in self.adj_list:
            self.adj_list[vertex1].add(vertex_it_points_to)
            self.adj_list[vertex1].add(vertex1)
           

            
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
            print(f"{vertex}: ", end="")
            self.adj_list[vertex].print_list()


g = DirectedGraph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)

g.add_directed_edge(1,2)
g.add_directed_edge(2,4)
g.add_directed_edge(3,2)
g.add_directed_edge(3,1)
g.add_directed_edge(4,1)
g.add_directed_edge(4,5)
g.add_directed_edge(5,3)


g.print()