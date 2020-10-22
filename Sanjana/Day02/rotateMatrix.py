def mirror(n: int, arr: [[int]]) -> [[int]]:
    for i in range(n):
        for j in range(n // 2):
            arr[i][j], arr[i][n - 1 - j] = arr[i][n - 1 - j], arr[i][j]
    return arr

def transpose(n: int, arr: [[int]]) -> [[int]]:
    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr

def display(arr: [[int]]):
    for row in arr:
        print(*row)

n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])
 
print()
display(arr)
print()
display(mirror(n, transpose(n, arr))) # rotate 90 degrees clockwise
print()
display(transpose(n, mirror(n, arr))) # rotate 90 degrees anti-clockwise

'''

Given a n x n 2D matrix, rotate it 90 degrees in clockwise or anti-clockwise direction without using extra space

Time complexity = O(N ^ 2)
Space complexity = O(1)

'''
