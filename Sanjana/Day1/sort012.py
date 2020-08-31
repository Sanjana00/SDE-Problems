def dutchNationalFlag(n: int, arr: [int]) -> [int]:
    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    return arr

n = int(input())
arr = [int(x) for x in input().split()]
print(*dutchNationalFlag(n, arr))
