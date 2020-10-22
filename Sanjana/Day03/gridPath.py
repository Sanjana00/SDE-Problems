from math import factorial

def gridPaths(row: int, col: int) -> int:
    return factorial(row + col - 2) // (factorial(row - 1) * factorial(col - 1))
    
row, col = [int(x) for x in input().split()]
print(gridPaths(row, col))


'''

Problem: Count the number of unique paths possible when moving from the (0, 0) position in a m x n dimension 2D matrix to the (m - 1, n - 1) position
(from upper left corner to lower right corner) if you can only move in rightward and downward directions.

Explanation: Each path can be thought of as a unique sequence of right moves (R) and down moves (D).
The number of right moves is (n - 1) and the number of down moves is (m - 1).
Total number of moves = n - 1 + m - 1 = n + m - 2
Therefore, the answer is the number of permutations possible in a sequence of (n - 1) R and (m - 1) D.

A string of length l with c1 present a times and c2 present b times has l!/(a!b!) number of unique permutations.

The factorial function of the math module has been used as it is faster (C type implementation).

'''
