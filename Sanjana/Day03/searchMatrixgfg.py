def searchMatrix(m: int, n: int, ele: int, arr: [[int]]) -> (int, int):
    col = n - 1
    while col >= 0:
        if arr[0][col] > ele:
            col -= 1
            continue
        # binary search
        low = 0
        high = m
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][col] == ele:
                return (mid, col)
            if arr[mid][col] > ele:
                high = mid - 1
            else:
                low = mid + 1
        if low > high:
            col -= 1
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
Find an element in a sorted 2D matrix of dimension m x n and return its position, or -1, -1 if not found.
The matrix is sorted in such a way that each row is in sorted ascending order, and each column is in sorted ascending order

Time complexity = O(n log m)
'''
