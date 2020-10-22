def merge(arr1 : [int], arr2 : [int]) -> [int]:
    n1, n2 = len(arr1), len(arr2)
    gap = n1 + n2
    while gap > 1:
        gap = (gap + 1) // 2
        i = 0
        while i < n1 + n2 - gap:
            if i < n1:
                if i + gap < n1:
                    if arr1[i] > arr1[i + gap]:
                        arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
                else:
                    if arr1[i] > arr2[i + gap - n1]:
                        arr1[i], arr2[i + gap - n1] = arr2[i + gap - n1], arr1[i]
            else:
                if arr2[i - n1] > arr2[i + gap - n1]:
                    arr2[i - n1], arr2[i + gap - n1] = arr2[i + gap - n1], arr2[i - n1]
            i += 1
    return arr1 + arr2

a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
print(merge(a1, a2))
    
'''

Merging two sorted arrays in sorted order without using extra space

Optimal solution

'''
