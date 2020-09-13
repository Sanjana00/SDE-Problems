def nextPermutation(arr: [int]) -> [int]:
    i = -2
    n = len(arr)
    while i >= -n:
        if arr[i] < arr[i + 1]:
            j = -1
            while j >= -n:
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    return arr[:i + 1] + arr[i + 1:][::-1]
                j -= 1
        i -= 1
    if i < -n:
        return arr[::-1]
    
arr = [int(x) for x in input().split()]
k = int(input())
for _ in range(k):
    print(*arr)
    arr = nextPermutation(arr)
    
'''
Find the next permutation

Assumption: all numbers are distinct

Eg.
1 2 3 -> 1 3 2 -> 2 1 3 -> 2 3 1 -> 3 1 2 -> 3 2 1 -> 1 2 3 -> ...

Algo:

Find number at least significant position i such that arr[i] < arr[i + 1]
Find number at least significant position j such that arr[j] > arr[i]

Swap arr[i] and arr[j] and reverse arr[i + 1:]

Time complexity = O(N)

'''
