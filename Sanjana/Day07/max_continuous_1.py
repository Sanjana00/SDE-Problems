def max_continuous_1(arr: [int], size: int) -> int:
    ans = 0
    count = arr[0]
    if size < 1:
        return 0
    p1, p2 = 0, 1
    if size < 2:
        return 1 if arr[0] == 1 else 0
    while p2 < size:
        if arr[p1] == 1:
            if arr[p2] == 0:
                ans = max(ans, count)
            else:
                count += 1
        elif arr[p2] == 1:
            count = 1
        p1 += 1
        p2 += 1
    return ans

arr = [int(x) for x in input()]
print(max_continuous_1(arr, len(arr)))
