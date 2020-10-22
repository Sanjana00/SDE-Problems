def mergeSort(arr: [int], temp: [int], left: int, right: int) -> int:
    if left >= right:
        return 0
    mid = (left + right) // 2
    return mergeSort(arr, temp, left, mid) + mergeSort(arr, temp, mid + 1, right) + merge(arr, temp, left, mid, right)

def merge(arr: [int], temp: [int], left: int, mid: int, right: int) -> int:
    i = left
    j = mid + 1
    k = left
    c = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            c += (mid - i + 1)
            k += 1
            j += 1
            
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for _ in range(left, right + 1):
        arr[_] = temp[_]
    return c

def countInversions(n: int, arr: [int]) -> int:
    return mergeSort(arr, [0] * n, 0, n - 1)

arr = [int(x) for x in input().split()]
print(countInversions(len(arr), arr))

'''
Count number of inversions in an array
i < j and arr[i] > arr[j]
'''
