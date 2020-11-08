class GraphColour:
    def __init__(self, vertices):
        self.V = vertices
        self.vertices = []
        self.graph = {}
        self.colour = {}
        self.get_graph()
        
    def get_graph(self):
        for _ in range(self.V):
            name = input('Enter name of node: ')
            self.graph[name] = input('Enter nodes {} is connected to: '.format(name)).split()
            self.colour[name] = 0
        self.vertices = list(self.graph.keys())
        
    def is_safe(self, v, c):
        return all(self.colour[neighbour] != c for neighbour in self.graph[self.vertices[v]])

    def m_colour(self, m, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, c):
                self.colour[self.vertices[v]] = c
                if self.m_colour(m, v + 1):
                    return True
                self.colour[self.vertices[v]] = 0
        return False
                
    def solve(self):
        if not self.m_colour(self.V, 0):
            print('No solution found')
        else:
            print(*self.colour.values())
            
n = int(input('Enter number of vertices: '))
g = GraphColour(n)

g.solve()
