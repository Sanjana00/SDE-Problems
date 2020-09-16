def searchMatrix(m: int, n: int, ele: int, arr: [[int]]) -> (int, int):
    low = 0
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] == ele:
            return (mid, 0)
        if arr[mid][0] > ele:
            high = mid - 1
        else:
            low = mid + 1
    row = high
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[row][mid] == ele:
            return (row, mid)
        if arr[row][mid] > ele:
            high = mid - 1
        else:
            low = mid + 1
    return (-1, -1)

m = int(input())
n = int(input())
arr = []
for _ in range(m):
    arr.append([int(x) for x in input().split()])
ele = int(input())
x, y = searchMatrix(m, n, ele, arr)
if (x, y) == (-1, -1):
    print("No such element found")
else:
    print("Element {} found at ({}, {})".format(ele, x, y))
    
    
'''

Find an element in a 2d matrix of dimension m x n, given matrix is in sorted ascending order

Time complexity = O(log m + log n)

'''
