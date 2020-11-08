class GraphColour:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [0] * vertices
        self.colour = [0] * vertices
        self.get_graph()
        
    def get_graph(self):
        for _ in range(self.V):
            self.graph[_] = [int(x) for x in input('Enter nodes {} is connected to: '.format(_)).split()]
        
    def is_safe(self, v, c):
        return all(self.colour[neighbour] != c for neighbour in self.graph[v])

    def m_colour(self, m, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, c):
                self.colour[v] = c
                if self.m_colour(m, v + 1):
                    return True
                self.colour[v] = 0
        return False
                
    def solve(self):
        if not self.m_colour(self.V, 0):
            print('No solution found')
        else:
            print(*self.colour)
            
n = int(input('Enter number of vertices: '))
g = GraphColour(n)

g.solve()
