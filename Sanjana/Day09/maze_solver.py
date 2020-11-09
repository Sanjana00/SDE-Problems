class Maze:
    def __init__(self, n):
        self.size = n
        self.map = [[0] * n for _ in range(n)]
        self.get_maze()
        
    def is_valid(self, x, y):
        return x > -1 and x < self.size and y > -1 and y < self.size and self.map[x][y] != '#'
    
    def solve_maze(self, x, y):
        if not self.is_valid(x, y):
            return False
        if self.map[x][y] == 'G':
            return True
        self.map[x][y] = '+'
        if self.solve_maze(x + 1, y):
            return True
        if self.solve_maze(x, y + 1):
            return True
        if self.solve_maze(x - 1, y):
            return True
        if self.solve_maze(x, y - 1):
            return True
        
        self.map[x][y] = '.'
        return False
    
    def display(self):
        print()
        for row in self.map:
            print(*row)
        print()
    
    def find_start(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 'S':
                    return x, y
    
    def get_maze(self):
        for row in range(self.size):
            self.map[row] = list(input())
    
    def solve(self):
        self.display()
        x, y = self.find_start()
        self.solve_maze(x, y)
        self.map[x][y] = 'S'
        self.display()
            
n = int(input('n = '))
maze = Maze(n)

maze.solve()
