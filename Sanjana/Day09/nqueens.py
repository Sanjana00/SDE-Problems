class NQueens:
    
    def __init__(self, n):
        self.n = n
        self.size = n ** 2
        self.queen_pos = []
        
    def is_safe(self, i):
        return self.safe_rows(i) and self.safe_cols(i) and self.safe_diag(i)
    
    def safe_rows(self, i):
        for pos in self.queen_pos:
            if pos // self.n == i // self.n:
                return False
        return True
    
    def safe_cols(self, i):
        for pos in self.queen_pos:
            if pos % self.n == i % self.n:
                return False
        return True
    
    def get_diags(self, i):
        positions = set()
        edges = set([i for i in range(0, self.n)] + [i for i in range(self.size - self.n, self.size)] + [i for i in range(0, self.size, self.n)] + [i for i in range(self.n - 1, self.size, self.n)])
        for _ in range(i - self.n + 1, -1, 1 - self.n):
            positions.add(_)
            if _ in edges:
                break
        for _ in range(i + self.n - 1, self.size + 1, self.n - 1):
            positions.add(_)
            if _ in edges:
                break
        for _ in range(i - self.n - 1, -1, -1 - self.n):
            positions.add(_)
            if _ in edges:
                break
        for _ in range(i + self.n + 1, self.size + 1, self.n + 1):
            positions.add(_)
            if _ in edges:
                break
        return positions
    
    def safe_diag(self, i):
        positions = self.get_diags(i)
        for pos in self.queen_pos:
            if pos in positions:
                return False
        return True
    
    def solve_backtrack(self):
        if len(self.queen_pos) == self.n:
            return True
        for i in range(self.size):
            if not self.is_safe(i):
                continue
            self.queen_pos.append(i)
            if self.solve_backtrack():
                return True
            self.queen_pos.remove(i)
        return False
    
    def solve(self):
        if not self.solve_backtrack():
            print('Could not solve')
        else:
            self.display()
    
    def display(self):
        rows = [pos // self.n for pos in self.queen_pos]
        cols = [pos % self.n for pos in self.queen_pos]
        pos = 0
        for i in range(self.n):
            row = ['-'] * self.n
            row[cols[pos]] = 'Q'
            print(' '.join(row))
            pos += 1
            
n = int(input())
game = NQueens(n)
game.solve()
