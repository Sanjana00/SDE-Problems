def searchMatrix(m: int, n: int, ele: int, arr: [[int]]) -> (int, int):
    low = 0
    high = m * n - 1
    while low <= high:
        mid = (low + high) // 2
        x, y = divmod(mid, n)
        if arr[x][y] == ele:
            return (x, y)
        if arr[x][y] > ele:
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
Find element in a 2D matrix of dimension m x n where all elements are in sorted ascending order (sorted array if unrolled).

Time complexity = O(log(m * n)) = O(log m +  log n)
'''
