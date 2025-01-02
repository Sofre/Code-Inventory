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


g = Graph()

nodes = [
    "Rickon-Stark", "Jojen-Reed", "Meera-Reed", "Bran-Stark", "Hodor",
    "Theon-Greyjoy", "Ramsay-Snow", "Jon-Snow", "Ygritte", "Tormund",
    "Mance-Rayder", "Aemon-Targaryen", "Samwell-Tarly", "Pypar",
    "Jeor-Mormont", "Qhorin-Halfhand", "Gilly", "Arya-Stark", "Gendry",
    "Hot-Pie", "Robb-Stark", "Catelyn-Stark", "Sansa-Stark", "Eddard-Stark",
    "Robert-Baratheon", "Renly-Baratheon", "Stannis-Baratheon", "Melisandre",
    "Davos-Seaworth", "Tyrion-Lannister", "Jaime-Lannister", "Cersei-Lannister",
    "Tywin-Lannister", "Joffrey-Baratheon", "Tommen-Baratheon", "Sandor-Clegane",
    "Bronn", "Varys", "Margarey-Tyrell", "Brienne-of-Tarth", "Drogo",
    "Daenerys-Targaryen", "Jorah-Mormont", "Irri", "Hizdahr-zo-Loraq", "Barristan-Selmy"
]


edges = [
    ("Rickon-Stark", "Bran-Stark"), ("Jojen-Reed", "Bran-Stark"),
    ("Meera-Reed", "Bran-Stark"), ("Bran-Stark", "Hodor"),
    ("Theon-Greyjoy", "Ramsay-Snow"), ("Bran-Stark", "Jon-Snow"),
    ("Jon-Snow", "Ygritte"), ("Jon-Snow", "Tormund"),
    ("Jon-Snow", "Jeor-Mormont"), ("Jeor-Mormont", "Samwell-Tarly"),
    ("Jon-Snow", "Aemon-Targaryen"), ("Samwell-Tarly", "Gilly"),
    ("Arya-Stark", "Gendry"), ("Arya-Stark", "Hot-Pie"),
    ("Robb-Stark", "Catelyn-Stark"), ("Robb-Stark", "Jon-Snow"),
    ("Catelyn-Stark", "Eddard-Stark"), ("Eddard-Stark", "Sansa-Stark"),
    ("Eddard-Stark", "Robert-Baratheon"), ("Robert-Baratheon", "Renly-Baratheon"),
    ("Renly-Baratheon", "Stannis-Baratheon"), ("Stannis-Baratheon", "Melisandre"),
    ("Stannis-Baratheon", "Davos-Seaworth"), ("Sansa-Stark", "Tyrion-Lannister"),
    ("Tyrion-Lannister", "Jaime-Lannister"), ("Jaime-Lannister", "Cersei-Lannister"),
    ("Cersei-Lannister", "Tywin-Lannister"), ("Tywin-Lannister", "Joffrey-Baratheon"),
    ("Tywin-Lannister", "Tommen-Baratheon"), ("Sansa-Stark", "Sandor-Clegane"),
    ("Tyrion-Lannister", "Bronn"), ("Tyrion-Lannister", "Varys"),
    ("Margarey-Tyrell", "Sansa-Stark"), ("Margarey-Tyrell", "Tommen-Baratheon"),
    ("Jaime-Lannister", "Brienne-of-Tarth"), ("Drogo", "Daenerys-Targaryen"),
    ("Daenerys-Targaryen", "Jorah-Mormont"), ("Daenerys-Targaryen", "Irri"),
    ("Hizdahr-zo-Loraq", "Daenerys-Targaryen"), ("Barristan-Selmy", "Daenerys-Targaryen")
]


def got_relationship(character):
    graph = Graph()
    
    for node in nodes:
        graph.add_vertex(node)
            
    
    for edge in edges:
        graph.add_edge(edge[0],edge[1])


    if character not in graph.adj_list:
        print(f"{character} not in list")
    else:
        for neighbor in graph.adj_list[character]:
            print(f"Interactions for {character}: ",[f"{neighbor}"])
        print()
    

    
    

got_relationship("Robert-Baratheon") 
    

