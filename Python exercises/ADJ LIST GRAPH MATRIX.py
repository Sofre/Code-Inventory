#ADJ LIST GRAPH MATRIX
# REPRESENTS IF THERE IS A EDGE OR NOT 
# RETURNS TRUE OR FALSE IN 1 and 0 and makes it into a matrix
class GraphMatrix:
    def __init__(self):
        self.vert = []
        self.adj_matrix = []

    def add_vertex(self,vertex):
        self.vert.append(vertex)
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0]*len(self.vert))
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.vert and vertex2 in  self.vert:
            idx1 = self.vert.index(vertex1)
            idx2 = self.vert.index(vertex2)
            self.adj_matrix[idx1][idx2] = 1
            self.adj_matrix[idx2][idx1] = 1
        else:
            print("One or both vert not found")

    def remove_edge(self,vertex1,vertex2):
         if vertex1 in self.vert and vertex2 in  self.vert:
            idx1 = self.vert.index(vertex1)
            idx2 = self.vert.index(vertex2)
            self.adj_matrix[idx1][idx2] = 0
            self.adj_matrix[idx2][idx1] = 0
         else:
            print("One or both vert not found")

    def remove_vertex(self,vertex):
        if vertex in self.vert:
            idx = self.vert.index(vertex)
            self.adj_matrix.pop(idx)
            for row in self.adj_matrix:
                row.pop(idx)
            self.vert.remove(vertex)
        else:
            print("vert not found")
    
    def print(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                print(self.adj_matrix[i][j],end=" ")
            print()

g = GraphMatrix()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.print()