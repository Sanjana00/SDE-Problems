def count_conflicts(arr: [int], dep: [int], size: int) -> int:
    count = 0
    ans = 0
    i, j = 0, 0
    arr.sort()
    dep.sort()
    while i < size and j < size:
        if arr[i] <= dep[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans, count)
    return ans

arr = [int(time.replace(':', '')) for time in input().split()]
dep = [int(time.replace(':', '')) for time in input().split()]

print(count_conflicts(arr, dep, len(dep)))
