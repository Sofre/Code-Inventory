#United States of America Airport Passanger Graph System
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
            print(current.get_data(), end=" , ")
            current = current.get_next()
        print("")
    


class DirectedWeightedGraph:
    def __init__(self):
        self.adj_list = {}
        self.followers_dict = {}
        self.following_dict = {}
        
        

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()
            

    def add_edge(self, vertex1, vertex_it_points_to,weight):
        if vertex1 in self.adj_list and vertex_it_points_to in self.adj_list:
            self.adj_list[vertex1].add((vertex_it_points_to,weight))
            
        else:
            print("One or both vertices not found in graph")

    def remove_edge(self, vertex1, vertex_it_points_to,weight):
        if vertex1 in self.adj_list and vertex_it_points_to in self.adj_list:
            self.adj_list[vertex1].remove(vertex_it_points_to)
            self.adj_list[vertex1].remove(weight)
        else:
            print("One or both vertices not found in the graph")

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
                self.adj_list[vertex].remove(neighbor)
            del self.adj_list[vertex]

           
            

    def count_vertices(self):
        print(len(self.adj_list))

    def print(self):
        for vertex in self.adj_list:
            print(f"{vertex}: ", end="")
            self.adj_list[vertex].print_list()


g = DirectedWeightedGraph()

for city in ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']:
    g.add_vertex(city)

g.add_edge('New York', 'Chicago', 0.9)
g.add_edge('New York', 'Phoenix', 0.8)
g.add_edge('Los Angeles', 'New York', 0.5)
g.add_edge('Los Angeles', 'Chicago', 0.6)
g.add_edge('Chicago', 'New York', 1.0)
g.add_edge('Chicago', 'Phoenix', 0.7)
g.add_edge('Houston', 'New York', 0.5)
g.add_edge('Houston', 'Phoenix', 0.4)
g.add_edge('Phoenix', 'Houston', 0.2)
g.add_edge('Phoenix', 'Philadelphia', 0.5)
g.add_edge('Philadelphia', 'Houston', 0.6)
g.add_edge('Philadelphia', 'Phoenix', 0.4)

print("US Airports Graph:")
g.print()



def numberofpassengers_adj_list(g):
    vertex_passenger_sums = {}  
    
    
    for x, linked_list in g.adj_list.items():
        current = linked_list.head  
        sum_of_passengers = 0  
        
        
        while current is not None:
           
            neighbor, weight = current.get_data()
            sum_of_passengers += weight  
            
            current = current.get_next()  
        
        
        vertex_passenger_sums[x] = float(sum_of_passengers)
    
   
    return vertex_passenger_sums

print()
passenger_sums = numberofpassengers_adj_list(g)
print("Outgoing passangers for each airport: ")
for vertex, sum_passengers in passenger_sums.items():
    print(f"{vertex}: {sum_passengers} million passangers")

    
 
