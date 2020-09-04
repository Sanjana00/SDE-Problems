def nextRow(row: [int], n: int) -> [int]:
    left = [0] + row
    right = row + [0]
    return [left[i] + right[i] for i in range(n)]

def pascalTriangle(n: int) -> [[int]]:
    pascal = [[1]]
    for i in range(n - 1):
        pascal.append(nextRow(pascal[-1], i + 2))
    return pascal

n = int(input())
for row in pascalTriangle(n):
    print(*row)
    
'''

I prefer to do this particular problem in the pythonic fashion!

'''
