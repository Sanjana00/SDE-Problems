def merge(arr1 : [int], arr2 : [int]) -> [int]:
    p1 = 0
    n1, n2 = len(arr1), len(arr2)
    while p1 < n1:
        if arr2[0] < arr1[p1]:
            arr1[p1], arr2[0] = arr2[0], arr1[p1]
            k = 0
            while k + 1 < n2 and arr2[k] > arr2[k + 1]:
                arr2[k + 1], arr2[k] = arr2[k], arr2[k + 1]
                k += 1
        p1 += 1
    return arr1 + arr2
    

'''

Merge two sorted arrays using O(1) space in sorted order

This is not the optimal solution

'''
