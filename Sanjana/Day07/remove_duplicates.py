def remove_duplicates(arr: [int], size: int) -> [int]:
    p1, p2 = 0, 1
    if size < 2:
        return arr
    while p2 < size:
        while arr[p2] == arr[p1]:
            arr.pop(p2)
            size -= 1
        p1 += 1
        p2 += 1
    return arr

arr = [int(x) for x in input().split()]
arr.sort()
print(*remove_duplicates(arr, len(arr)))
