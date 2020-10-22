n = int(input())
arr = sorted([int(x) for x in input().split()])
l = len(arr)
results = []
i = 0
while i < l - 1:
    x = arr[i]
    j = i + 1
    while j < l:
        y = arr[j]
        left = j + 1
        right = l - 1
        target = n - arr[i] - arr[j]
        while left < right:
            if arr[left] + arr[right] == target:
                results.append([arr[i], arr[j], arr[left], arr[right]])
                z1 = arr[left]
                z2 = arr[right]
                while left < l and arr[left] == z1:
                    left += 1
                while right > -1 and arr[right] == z2:
                    right -= 1
            elif arr[left] + arr[right] < target:
                z = arr[left]
                while left < l and arr[left] == z:
                    left += 1
            else:
                z = arr[right]
                while right > -1 and arr[right] == z:
                    right -= 1
        while j < l and arr[j] == y:
            j += 1
    while i < l and arr[i] == x:
        i += 1
for result in results:
    print(*result)
    
'''

Given an array and target, find all possible combinations of four array elements which add up to the target

Approach: Sort array, keep two pointers and use two pointer method for finding the sum of two elements in the remaining sorted array

Time complexity = O(n log n + n^3)

'''
