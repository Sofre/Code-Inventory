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
    


class DirectedGraph:
    def __init__(self):
        self.adj_list = {}
        self.followers_dict = {}
        self.following_dict = {}
        

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()
            self.followers_dict[vertex] = []
            self.following_dict[vertex] = []

    def add_directed_edge(self, vertex1, vertex_it_points_to):
        if vertex1 in self.adj_list and vertex_it_points_to in self.adj_list:
            self.adj_list[vertex1].add(vertex_it_points_to)
            self.following_dict[vertex1].append(vertex_it_points_to)
            self.followers_dict[vertex_it_points_to].append(vertex1)
        else:
            print("One or both vertices not found in graph")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].remove(vertex2)
            self.following_dict[vertex1].remove(vertex2)
            self.followers_dict[vertex2].remove(vertex1)
        else:
            print("One or both vertices not found in the graph")

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.followers_dict[neighbor].remove(vertex)
                self.following_dict[vertex].remove(neighbor)
            del self.adj_list[vertex]
            del self.followers_dict[vertex]
            del self.following_dict[vertex]

    def count_vertices(self):
        print(len(self.adj_list))

    def print(self):
        for vertex in self.adj_list:
            print(f"{vertex}: ", end="")
            self.adj_list[vertex].print_list()

  
    def followers(self, vertex):
        if vertex in self.followers_dict:
            followers_list = self.followers_dict[vertex]
            followers_count = len(followers_list)
            return followers_count, followers_list
        else:
            print("Vertex not found")
            return 0, []
            
            

   
    def following(self, vertex):
        if vertex in self.following_dict:
            following_list = self.following_dict[vertex]
            following_count = len(following_list)
            return following_count,following_list
        else:
            print("Vertex not found")
            return []

# Test the graph
g = DirectedGraph()

g.add_vertex("Sofie")
g.add_vertex("Julie")
g.add_vertex("Ava")
g.add_vertex("Alex")
g.add_vertex("David")
g.add_directed_edge("Sofie", "Julie")
g.add_directed_edge("Sofie", "Alex")
g.add_directed_edge("Julie", "Ava")
g.add_directed_edge("Ava", "Sofie")
g.add_directed_edge("Alex", "David")
g.add_directed_edge("Alex", "Julie")
g.add_directed_edge("Alex", "Ava")
g.add_directed_edge("David", "Alex")

# Print the graph
g.print()

# Test followers and following
print("Followers of Alex:", g.followers("Alex"))
print("Following of Sofie:", g.following("Sofie"))



# Test the graph
g = DirectedGraph()

g.add_vertex("Sofie")
g.add_vertex("Julie")
g.add_vertex("Ava")
g.add_vertex("Alex")
g.add_vertex("David")
g.add_directed_edge("Sofie", "Julie")
g.add_directed_edge("Sofie", "Alex")
g.add_directed_edge("Julie", "Ava")
g.add_directed_edge("Ava", "Sofie")
g.add_directed_edge("Alex", "David")
g.add_directed_edge("Alex", "Julie")
g.add_directed_edge("Alex", "Ava")
g.add_directed_edge("David", "Alex")
g.print()

print("Followers of Alex:", g.followers("Alex"))
print("Following of Sofie:", g.following("Sofie"))

