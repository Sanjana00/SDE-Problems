def three_sum(arr: [int], size: int) -> [[int]]:
    triplets = []
    arr.sort()
    for i, ele in enumerate(arr):
        left = i + 1
        right = size - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                continue
            if s < 0:
                left += 1
                continue
            right -= 1
            
    return triplets

arr = [int(x) for x in input().split()]
triplets = three_sum(arr, len(arr))

for triplet in triplets:
    print(*triplet)
    
if len(triplets) == 0:
    print('None found')
