def trap_water(arr: [int], size: int) -> int:
    water, rmax, lmax = 0, 0, 0
    right_max = [0]
    left_max = [0]
    for ele in arr[:-1]:
        lmax = max(lmax, ele)
        left_max.append(lmax)
    for ele in arr[:0:-1]:
        rmax = max(rmax, ele)
        right_max.append(rmax)
    for i in range(size):
        water += max(min(left_max[i], right_max[size - i - 1]) - arr[i], 0)
    return water

arr = [int(x) for x in input().split()]
print(trap_water(arr, len(arr)))
