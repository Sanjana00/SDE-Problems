def trap_water(arr: [int], size: int) -> int:
    water, rmax, lmax, low, high = 0, 0, 0, 0, size - 1
    while low <= high:
        if arr[low] < arr[high]:
            lmax = max(lmax, arr[low])
            water += max(lmax - arr[low], 0)
            low += 1
            continue
        rmax = max(rmax, arr[high])
        water += max(rmax - arr[high], 0)
        high -= 1
    return water

arr = [int(x) for x in input().split()]
print(trap_water(arr, len(arr)))
