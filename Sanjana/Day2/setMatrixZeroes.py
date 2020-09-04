def setMatrixZeroes(arr: [[int]]) -> [[int]]:
    m = len(arr)
    n = len(arr[0])
    row = 0 in arr[0]
    col = False
    for i in range(1, m):
        if arr[i][0] == 0:
            col = True
        for j in range(1, n):
            if arr[i][j] == 0:
                arr[0][j] = 0
                arr[i][0] = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if arr[i][0] == 0 or arr[0][j] == 0:
                arr[i][j] = 0
        if col:
            arr[i][0] = 0
        if row:
            arr[0][j] = 0
    return arr

arr = []
m = int(input())
for _ in range(m):
    arr.append([int(x) for x in input().split()])
for row in setMatrixZeroes(arr):
    print(*row)
    
'''

Given a matrix of integers, if an element equal to zero, change all elements in same row and column to 0.
row and col boolean values hold true if the first row or first column of matrix contain a 0.
Space complexity O(1)
Time complexity O(M x N)

'''
